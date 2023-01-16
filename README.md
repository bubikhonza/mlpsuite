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
- Connect to spark master and run following: `/opt/bitnami/spark/bin/spark-submit --master spark://spark:7077 --py-files /shared_core/dependencies.zip /shared_core/run_train_job.py`



## Modifying input data
If input data for training needs transformation, you can use jupyter container (jupyterlab) for this purpose - /shared_usr/* contains directory shared between every container

## Infrastructure:

Application consists of several *Docker containers*, each container has its own responsibility

##### Input data Kafka container:
* Serves as messaging queue for input data.

##### Output data Kafka container:
* Serves as messaging queue for transformed data.

##### Spark Driver:
* Part of Spark streaming engine

##### Spark Worker/s:
* Part of Spark streaming engine

##### Log aggregator container:
* Takes care of managing logs.

##### Grafana container:
* Serves as data visualizer.

##### Persistant storage container:
* Persistant storage for historical data.

##### Application logic container:
* Container that is responsible for business logic and also takes care of loading proper transformers/evaluators.


##### Data API container: 
* Publishing messages
* Reading transformed messages
* Accessing logs
* Accessing persistant storage
    
 
    


