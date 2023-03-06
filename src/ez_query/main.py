from ez_query.config import load_config
from ez_query.processor import Processor


def run():
    config = load_config()
    Processor(config).start()

if __name__ == "__main__":
    run()
