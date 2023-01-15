from pyspark.sql.types import StructType
from pyspark.sql import DataFrame
from pyspark.sql import SparkSession


class DataLoader:
    @staticmethod
    def load_csv(path: str, header: str, schema: StructType) -> DataFrame:
        spark = SparkSession.builder.appName("Pipeliner").getOrCreate()
        df = spark.sparkContext.read.format("com.databricks.spark.csv").schema(
            schema).option("header", header).load(path)
        return df