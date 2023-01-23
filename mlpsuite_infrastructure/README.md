## MLPSuite - Infrastructure
Docker container orchestration with spark and kafka.

### Installation
- install Docker
- docker compose up -d

### Testing the installation

#### To test Kafka
- install https://www.kafkatool.com/index.html
- add broker, topic and publish message

#### To test Spark: 
Connect to spark master and run following:
`/opt/bitnami/spark/bin/spark-submit --master spark://spark:7077 /opt/bitnami/spark/examples/src/main/python/pi.py`

### Running the pipeline using MLPSuite engine ###
*Make sure to place all dependencies (config, jar, zip, py files) in corresponding directories*
#### Training:
- Connect to spark master and run following: `/opt/bitnami/spark/bin/spark-submit --master spark://spark:7077 --py-files /shared/usr/dependencies.zip /shared/core/run_train_job.py`

### Prediction:
- Connect to spark master and run following: `/opt/bitnami/spark/bin/spark-submit --conf spark.jars.ivy=/opt/bitnami/spark/ivy --jars /shared/core/spark-sql-kafka-0-10_2.12-3.3.1.jar --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.1 --master spark://spark:7077 --py-files /shared/usr/dependencies.zip /shared/core/run_predict_job.py`

### Exploring and editing data
If you need to explore or edit the training data, you can use jupyter container for this purpose - /shared/usr/* contains directory shared between every container. You can then reference it in pipeline.yml


