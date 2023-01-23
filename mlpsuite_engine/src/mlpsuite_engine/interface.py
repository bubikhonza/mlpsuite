from pyspark.ml import Pipeline, PipelineModel
from pyspark.sql import SparkSession
from collections import ChainMap
from mlpsuite_engine.stage import Stage
from mlpsuite_engine.data_loader import DataLoader
from pyspark.sql import DataFrame
import pyspark.sql.functions as F
import yaml
import logging


class Interface:
    def __init__(self, config_path: str:
        self.__config = DataLoader.load_yml(config_path)
        self.__stages_conf = self.__config["stages"]
        self.__train_conf = dict(ChainMap(*self.__config["train"]))
        self.__predict_conf = dict(ChainMap(*self.__config["predict"]))
        self.__train_data_schema = dict(ChainMap(*self.__train_conf["schema"]))
        self.__predict_data_schema = dict(ChainMap(*self.__predict_conf["schema"]))

    def __create_pipeline(self) -> Pipeline:
        pyspark_stages = []
        for s_d in self.__stages_conf:
            stage_attributes = dict(ChainMap(*next(iter(s_d.values()))))
            stage = Stage(**stage_attributes)
            pyspark_stages.append(stage.construct_pyspark_obj())

        return Pipeline(stages=pyspark_stages)

    def __create_pyspark_train_schema(self):
        from pyspark.sql.types import StringType, StructField, StructType, TimestampType, DoubleType, IntegerType
        schema = StructType()
        for k, v in self.__train_data_schema.items():
            schema.add(StructField(k, eval(v)(), nullable=True))
        return schema

    def __create_pyspark_predict_schema(self):
        from pyspark.sql.types import StringType, StructField, StructType, TimestampType, DoubleType, IntegerType
        schema = StructType()
        for k, v in self.__predict_data_schema.items():
            schema.add(StructField(k, eval(v)(), nullable=True))
        return schema

    def __load_train_data(self) -> DataFrame:
        path = self.__train_conf["path"]
        header = self.__train_conf["header"]
        schema = self.__create_pyspark_train_schema()
        return DataLoader.load_csv(path, header, schema)

    def run_train(self) -> None:
        spark = SparkSession.builder.appName("Pipeliner").getOrCreate()

        pipeline = self.__create_pipeline()
        fitted_pipeline = pipeline.fit(self.__load_train_data())
        fitted_pipeline.save(self.__train_conf["pipeline_output"])
        spark.stop()

    def run_predict(self) -> None:
        logger = logging.getLogger('pyspark')
        logger.error("My test info statement")
        spark = SparkSession.builder.appName("Pipeliner").getOrCreate()
        pipeline = PipelineModel.load(self.__predict_conf["pipeline_path"])
        input_stream_df = spark \
            .readStream \
            .format("kafka") \
            .option("kafka.bootstrap.servers", "kafka:9092") \
            .option("subscribe", "input") \
            .option("failOnDataLoss", "false") \
            .load()

        schema = self.__create_pyspark_predict_schema()
        df = input_stream_df.selectExpr("CAST(value as STRING)")
        df = df.select(
            F.from_json(F.col("value"), schema).alias("sample")
        )
        df = df.select("sample.*")
        result = pipeline.transform(df)
        result = result.select([F.col(c).cast("string") for c in result.columns])
        result = result.withColumn("value", F.to_json(F.struct("*")).cast("string"),)
        query = result \
            .writeStream \
            .format("kafka") \
            .option("kafka.bootstrap.servers", "kafka:9092") \
            .option("checkpointLocation", "/shared/core/checkpoint") \
            .option("topic", "output") \
            .start()

        query.awaitTermination()
