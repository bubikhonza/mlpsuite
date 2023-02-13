### Installation
- install Docker
- docker compose up -d

### Testing the installation

#### To test Kafka
You can use kafkatool (https://www.kafkatool.com/index.html) to test kafka. 

#### To test Spark: 
Connect to spark master and run following:
`/opt/bitnami/spark/bin/spark-submit --master spark://spark:7077 /opt/bitnami/spark/examples/src/main/python/pi.py`

### Running the pipeline using MLPSuite engine ###
*Make sure to place all dependencies (config, jar, zip, py files) in corresponding directories*
#### Training:
Connect to spark master and run following: `/opt/bitnami/spark/bin/spark-submit --master spark://spark:7077 --py-files /shareddependencies.zip /shared/run_train_job.py`

Result of this job is a pipeline model stored on path specified in engine configuration.
#### Prediction:
Connect to spark master and run following: `/opt/bitnami/spark/bin/spark-submit --conf spark.jars.ivy=/opt/bitnami/spark/ivy --jars /shared/spark-sql-kafka-0-10_2.12-3.3.1.jar --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.1 --master spark://spark:7077 --py-files /shareddependencies.zip /shared/run_predict_job.py`

After executing this job, every input you send to input 
kafka will be transformed by the pipeline model and sent to output kafka.
Kafka's and pipeline model are specified in engine configuration.
### Exploring and editing data
If you need to explore or edit the training data, you can use jupyter container for this purpose - /shared* contains directory shared between every container.
