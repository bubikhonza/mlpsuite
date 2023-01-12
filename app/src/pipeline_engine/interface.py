from pyspark.ml import Pipeline
from pyspark.sql import SparkSession
from collections import ChainMap
from pipeline_engine.stage import Stage
import yaml

def load_yml() -> dict:
    data_loaded = {}
    with open("/shared_usr/pipeline.yml", 'r') as stream:
        data_loaded = yaml.safe_load(stream)
    return data_loaded


def create_pipeline(config: dict) -> Pipeline:
    stages_dict = config["stages"]
    pyspark_stages = []
    for s_d in stages_dict:
        stage_attributes = dict(ChainMap(*next(iter(s_d.values()))))
        stage = Stage(**stage_attributes)
        pyspark_stages.append(stage.construct_pyspark_obj())

    return Pipeline(stages=pyspark_stages)

def run_pipeline() -> None:
    spark = SparkSession.builder.appName("Pipeliner").getOrCreate()
    config = load_yml()
    pipeline = create_pipeline(config)
    spark.stop()
