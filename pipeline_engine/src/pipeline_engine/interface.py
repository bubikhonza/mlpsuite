from pyspark.ml import Pipeline
from pyspark.sql import SparkSession
from collections import ChainMap
from pipeline_engine.stage import Stage
from pipeline_engine.data_loader import DataLoader
from pyspark.sql import DataFrame
import yaml

class PipelineInterface:
    def __init__(self):
        pass
    
    def __create_pipeline(self, stages_dict: dict) -> Pipeline:
        pyspark_stages = []
        for s_d in stages_dict:
            stage_attributes = dict(ChainMap(*next(iter(s_d.values()))))
            stage = Stage(**stage_attributes)
            pyspark_stages.append(stage.construct_pyspark_obj())

        self.__pyspark_pipeline = Pipeline(stages=pyspark_stages)

    def __load_train_data(self, train_dict: dict) -> DataFrame:
        train_dict = dict(ChainMap(*train_dict))  # make dict form list
        print(train_dict)
        path = train_dict["path"]
        header = train_dict["header"]
        schema_dict = dict(ChainMap(*train_dict["schema"]))
        from pyspark.sql.types import StringType, StructField, StructType, TimestampType, DoubleType, IntegerType
        schema = StructType()
        for k, v in schema_dict.items():
            schema.add(StructField(k, eval(v)(), nullable=True))
        return DataLoader.load_csv(path, header, schema)


    def run_pipeline(self) -> None:
        spark = SparkSession.builder.appName("Pipeliner").getOrCreate()
        config = DataLoader.load_yml()
        pipeline = self.__create_pipeline(config["stages"])
        self.__load_train_data(config["train"])
        spark.stop()
