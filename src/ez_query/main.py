from config import load_config
from processor import Processor

config = load_config()
Processor(config).start()
