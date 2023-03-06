from typing import List
import logging
from prompt_toolkit.shortcuts import checkboxlist_dialog
from prompt_toolkit import prompt

from ez_query.config import Config
from ez_query.chatgpt_communicator import ChatGPTCommunicator
from ez_query.schema_req import SchemaRequester


class Processor:
    """Main loop which takes in user input and outputs results."""

    def __init__(self, config: Config):
        self.sr = SchemaRequester(config)
        self.chatgpt_comm = ChatGPTCommunicator(config)

    def start(self):
        tables = self._select_tables()
        if not tables:
            print("No tables were selected, exiting.")
            exit(0)

        q = self._get_question()
        if not q or len(q) == 0:
            print("No question asked, exiting.")
            exit(0)
            
        tables_info = [self.sr.schema_for_table(table) for table in tables]
        resp = self.chatgpt_comm.ask(tables_info, q)

        print()
        print(f"Total Tokens Used: {resp.total_tokens_used}")
        print("ChatGPT Response:")
        print(resp.message)

    def _get_question(self) -> str:
        return prompt("Please ask ChatGPT what SQL query to generate:\n")

    def _select_tables(self) -> List[str]:
        """Select which tables to feed ChatGPT prior to asking to generate a query."""
        tables = self.sr.tables
        options = [(table, table) for table in tables]

        selected_tables = checkboxlist_dialog(
            title="Select tables",
            text="Select which tables are relevant for your query. "
            "For ChatGPT to work best, I reccomend providing solely the tables necessary for the query to work.",
            values=options,
        ).run()

        return selected_tables

