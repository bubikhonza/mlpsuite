from pyspark.ml import Pipeline
from pyspark.sql import SparkSession
from collections import ChainMap
from pipeline_engine.stage import Stage
from pipeline_engine.data_loader import DataLoader
from pyspark.sql import DataFrame
import yaml


class PipelineInterface:
    def __init__(self):
        self.__config = DataLoader.load_yml()
        self.__stages_conf = self.__config["stages"]
        self.__train_conf = dict(ChainMap(*self.__config["train"])) 
        self.__predict_conf = dict(ChainMap(*self.__config["stages"])) 
        

    def __create_pipeline(self) -> Pipeline:
        pyspark_stages = []
        for s_d in self.__stages_conf:
            stage_attributes = dict(ChainMap(*next(iter(s_d.values()))))
            stage = Stage(**stage_attributes)
            pyspark_stages.append(stage.construct_pyspark_obj())

        return Pipeline(stages=pyspark_stages)

    def __load_train_data(self) -> DataFrame:
        path = self.__train_conf["path"]
        header = self.__train_conf["header"]
        schema_dict = dict(ChainMap(*self.__train_conf["schema"]))
        from pyspark.sql.types import StringType, StructField, StructType, TimestampType, DoubleType, IntegerType
        schema = StructType()
        for k, v in schema_dict.items():
            schema.add(StructField(k, eval(v)(), nullable=True))
        return DataLoader.load_csv(path, header, schema)

    def run_train(self) -> None:
        spark = SparkSession.builder.appName("Pipeliner").getOrCreate()
        
        pipeline = self.__create_pipeline()
        fitted_pipeline = pipeline.fit(self.__load_train_data())
        fitted_pipeline.save(self.__train_conf["pipeline_output"])
        spark.stop()

    def run_predict(self) -> None:
        spark = SparkSession.builder.appName("Pipeliner").getOrCreate()
        pipeline = Pipeline.load(self.__predict_conf["pipeline_path"])
        # run stream
