from pyspark.sql.types import StructType
from pyspark.sql import DataFrame
from pyspark.sql import SparkSession
import yaml


class DataLoader:
    @staticmethod
    def load_csv(path: str, header: str, schema: StructType) -> DataFrame:
        spark = SparkSession.builder.appName("Pipeliner").getOrCreate()
        df = spark.sparkContext.read.format("com.databricks.spark.csv").schema(
            schema).option("header", header).load(path)
        return df

    @staticmethod
    def load_yml(path: str = "/shared_usr/pipeline.yml") -> dict:
        data_loaded = {}
        with open(path, 'r') as stream:
            data_loaded = yaml.safe_load(stream)
        return data_loaded
