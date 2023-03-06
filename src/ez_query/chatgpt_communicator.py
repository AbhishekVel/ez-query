import os
from typing import List
import logging
from dataclasses import dataclass
import openai

from ez_query.config import Config
from ez_query.schema_req import TableInfo


@dataclass
class ChatGPTResponse:
    message: str
    total_tokens_used: int


class ChatGPTCommunicator():
    def __init__(self, config: Config):
        openai.api_key = config.openai_api_key

    def ask(self, tables_info: List[TableInfo], question) -> ChatGPTResponse:
        messages=[
            {"role": "system", "content": self._system_msg()},
            {"role": "user", "content": self._sql_tables_info_msg(tables_info)},
            {"role": "user", "content": question},
        ]

        logging.debug(messages)
        
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        return ChatGPTResponse(message=resp["choices"][0]["message"]["content"], total_tokens_used=resp["usage"]["total_tokens"]) 

    def _system_msg(self):
        return """
        You are a chatbot mean't for generating SQL queries. I will give you SQL tables
        and ask you to generate a query for me.
        """

    def _sql_tables_info_msg(self, tables_info: List[TableInfo]) -> str:
        msg = "Here are the SQL table schemas:\n"
        for table_info in tables_info:
            msg += str(table_info) + "\n"

        return msg

