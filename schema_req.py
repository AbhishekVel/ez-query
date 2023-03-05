import os
import logging
from typing import List, Dict
import functools as functools
from dataclasses import dataclass

import mysql.connector

from constants import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD


@dataclass
class ColumnInfo:
    field: str
    ctype: str
    null: str
    key: str
    default: str
    extra: str


class SchemaRequester:
    """
    Responsible for retrieving the table schemas from the DB.
    Note: only mySQL is currently supported.
    """

    def __init__(self):
        self.cnx = mysql.connector.connect(
            host=os.getenv(DB_HOST),
            user=os.getenv(DB_USER),
            password=os.getenv(DB_PASSWORD),
            database=os.getenv(DB_NAME),
        )

    def __del__(self):
        self.cnx.close()

    @functools.cache
    def schema_for_table(self, table: str) -> List[ColumnInfo]:
        logging.info(f"Getting schema for table {table}")
        csr = self.cnx.cursor()
        csr.execute(f"DESCRIBE {table};")
        schema = [
            ColumnInfo(field, ctype, null, key, default, extra)
            for (field, ctype, null, key, default, extra) in csr
        ]
        csr.close()

        return schema

    @functools.cached_property
    def tables(self) -> List[str]:
        logging.info(f"Getting list of tables")
        csr = self.cnx.cursor()
        csr.execute("SHOW TABLES;")
        tables = [table_name for (table_name,) in csr]
        csr.close()

        return tables
