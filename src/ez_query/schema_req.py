import os
import logging
from typing import List, Dict
import functools as functools
from dataclasses import dataclass
import mysql.connector

from ez_query.config import Config


@dataclass
class ColumnInfo:
    field: str
    ctype: str
    null: str
    key: str
    default: str
    extra: str

    COLUMN_NAMES = "Field, Type, Null, Key, Default, Extra"

    def __str__(self):
        return f"{self.field}, {self.ctype}, {self.null}, {self.key}, {self.default}, {self.extra}"

@dataclass
class TableInfo:
    name: str
    columns: List[ColumnInfo]

    def __str__(self):
        res = f"Table name: {self.name}\n"
        res += ColumnInfo.COLUMN_NAMES + "\n"
        for column in self.columns:
            res += str(column) + "\n"

        return res


class SchemaRequester:
    """
    Responsible for retrieving the table schemas from the DB.
    Note: only mySQL is currently supported.
    """

    def __init__(self, config: Config):
        self.cnx = mysql.connector.connect(
            host=config.db_host,
            user=config.db_user,
            password=config.db_pass,
            database=config.db_name
        )

    def __del__(self):
        self.cnx.close()

    @functools.cache
    def schema_for_table(self, table: str) -> TableInfo:
        logging.info(f"Getting schema for table {table}")
        csr = self.cnx.cursor()
        csr.execute(f"DESCRIBE {table};")
        columns = [
            ColumnInfo(str(field), str(ctype), str(null), str(key), str(default), str(extra))
            for (field, ctype, null, key, default, extra) in csr
        ]
        csr.close()

        return TableInfo(name=table, columns=columns)

    @functools.cached_property
    def tables(self) -> List[str]:
        logging.info(f"Getting list of tables")
        csr = self.cnx.cursor()
        csr.execute("SHOW TABLES;")
        tables = [str(table_name) for (table_name,) in csr]
        csr.close()

        return tables
