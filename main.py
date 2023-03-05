import os

from dotenv import load_dotenv
import openai

from constants import OPENAI_API_KEY
from schema_req import SchemaRequester

# Take environment variables from .env
load_dotenv()

openai.api_key = os.getenv(OPENAI_API_KEY)

print(
    openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"},
            {
                "role": "assistant",
                "content": "The Los Angeles Dodgers won the World Series in 2020.",
            },
            {"role": "user", "content": "Where was it played?"},
        ],
    )
)

sr = SchemaRequester()
schema = sr.schema_for_table(sr.tables[0])
print(schema)
