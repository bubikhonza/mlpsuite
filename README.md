## Anomaly detection and general data transformation pipeline

Aims to provide easy way to transform data via pyspark streaming ML pipeline, without the need of setting up complex infrastructure. Its primary purpose is to serve as anomaly detector, hovewer it can be used as any data transformation pipeline. 

### How to run ###
Connect to spark master and run following:
to test spark: 
`/opt/bitnami/spark/bin/spark-submit --master spark://spark:7077 /opt/bitnami/spark/examples/src/main/python/pi.py`

to run pipeline:
- `pip install -t dependencies -r requirements.txt`
- zip dependencies folder --- make sure packages are in zip root!
- `/opt/bitnami/spark/bin/spark-submit --master spark://spark:7077 --py-files /app/dependencies/dependencies.zip --conf spark.jars.ivy=/tmp/.ivy /app/src/main.py`


The solution above doesnt work, use this as temp:
- install packages (numpy) manually on worker/master
- `/opt/bitnami/spark/bin/spark-submit --master spark://spark:7077 /app/src/main.py`




###Infrastructure of this application consists of several *Docker containers*, each container has its own responsibility:###

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
    
 
    


