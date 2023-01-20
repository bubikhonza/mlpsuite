## Anomaly detection and general data transformation pipeline

Aims to provide easy way to transform data via pyspark streaming ML pipeline, without the need of setting up complex infrastructure. Its primary purpose is to serve as anomaly detector, hovewer it can be used as any data transformation ml pipeline. 

## Installation
- install Docker
- docker compose up -d

## Testing the installation

#### To test Kafka
- install https://www.kafkatool.com/index.html
- add broker, topic and publish message

#### To test Spark: 
Connect to spark master and run following:
`/opt/bitnami/spark/bin/spark-submit --master spark://spark:7077 /opt/bitnami/spark/examples/src/main/python/pi.py`

## Running the pipeline ###
- run `create_dependencies.bat`
#### Training:
- Connect to spark master and run following: `/opt/bitnami/spark/bin/spark-submit --master spark://spark:7077 --py-files /shared/core/dependencies.zip /shared/core/run_train_job.py`

#### Prediction:
- Connect to spark master and run following: `/opt/bitnami/spark/bin/spark-submit --conf spark.jars.ivy=/opt/bitnami/spark/ivy --jars /shared/core/spark-sql-kafka-0-10_2.12-3.3.1.jar --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.1 --master spark://spark:7077 --py-files /shared/core/dependencies.zip /shared/core/run_predict_job.py`



## Exploring and editing data
If you need to explore or edit the training data, you can use jupyter container for this purpose - /shared/usr/* contains directory shared between every container. You can then reference it in pipeline.yml


