import os

from dotenv import load_dotenv

from processor import Processor

# Take environment variables from .env
load_dotenv()

Processor().start()
