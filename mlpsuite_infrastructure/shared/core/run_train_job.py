from mlpsuite_engine.interface import Interface

interface = Interface("/shared/usr/pipeline.yml")


if __name__ == "__main__":
    interface.run_train()
