[<< MLPSuite home](../.)
## MLPSuite Engine

Core part of MLPSuite. Provides easy interface to build Pyspark ML pipelines from yaml file.

## Submitting to Spark
*NOTE: You can use - [MLPSuite Infrastructure](../mlpsuite_infrastructure) if you dont want to setup own infrastructure*
### main file
Engine exposes interface `interface.py` -> `Interface(path_to_config)`

Your `main.py` file for `spark-submit` should look like following:
```
from mlpsuite_engine.interface import Interface

interface = Interface(<path to yaml config>)

if __name__ == "__main__":
    # To run train:
    interface.run_train() 
```
If you want to run predictions: `interface.run_predict()`

### Submitting dependencies
Released zip version of engine must be added to spark-submit as `--py-files <path to dependencies.zip>`

Engine uses kafka for input and output. Find correct spark-sql-kafka package on maven: https://mvnrepository.com/ and use it in spark submit as `--jars <path to kafka jar> --packages <package Maven coordinates>`


### Configuration description:
TODO

### Development:
In order to build new zip with dependencies you can use helper batch script: `create_dependencies.bat`
