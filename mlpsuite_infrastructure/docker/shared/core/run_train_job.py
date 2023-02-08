from mlpsuite_engine.interface import Interface

# TODO: load path from env variable
interface = Interface("/shared/usr/pipeline.yml")

if __name__ == "__main__":
    interface.run_train()
