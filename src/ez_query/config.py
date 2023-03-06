import os
import argparse
from dataclasses import dataclass
from dotenv import load_dotenv

OPENAI_API_KEY = "OPENAI_API_KEY"
DB_HOST = "DB_HOST"
DB_USER = "DB_USER"
DB_PASSWORD = "DB_PASSWORD"
DB_NAME = "DB_NAME"

@dataclass
class Config:
    openai_api_key: str

    db_host: str
    db_user: str
    db_pass: str
    db_name: str

def load_config():
    # Take environment variables from .env
    load_dotenv()

    parser = argparse.ArgumentParser(description='SQL Query Generator powered by ChatGPT.')
    parser.add_argument(
            '--openai_api_key',
            required=False,
            type=str,
            help='OpenAI API Key',
            dest="openai_api_key")
    parser.add_argument(
            '--db_host',
            required=False,
            type=str,
            help='DB Host (i.e. localhost)',
            dest="db_host")
    parser.add_argument(
            '--db_user',
            required=False,
            type=str,
            help='DB User',
            dest="db_user")
    parser.add_argument(
            '--db_pass',
            required=False,
            type=str,
            help='DB Password',
            dest="db_pass")
    parser.add_argument(
            '--db_name',
            required=False,
            type=str,
            help='DB Name',
            dest="db_name")

    args = parser.parse_args()

    openai_api_key = args.openai_api_key or os.getenv(OPENAI_API_KEY)
    db_host = args.db_host or os.getenv(DB_HOST)
    db_user = args.db_user or os.getenv(DB_USER)
    db_pass = args.db_pass or os.getenv(DB_PASSWORD)
    db_name = args.db_name or os.getenv(DB_NAME)

    if not openai_api_key:
        print("Missing openai_api_key")
        exit(1)
    if not db_host:
        print("Missing db_host")
        exit(1)
    if not db_user:
        print("Missing db_user")
        exit(1)
    if not db_pass:
        print("Missing db_pass")
        exit(1)
    if not db_name:
        print("Missing db_name")
        exit(1)

    return Config(openai_api_key, db_host, db_user, db_pass, db_name)
