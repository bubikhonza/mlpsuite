from mlpsuite_engine.interface import Interface

# TODO: load path from env variable
interface = Interface("/sharedmlpsuite_engine_config.yaml")

if __name__ == "__main__":
    interface.run_predict()
