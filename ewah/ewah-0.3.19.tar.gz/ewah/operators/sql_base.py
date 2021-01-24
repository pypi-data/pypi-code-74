from ewah.operators.base import EWAHBaseOperator
from ewah.constants import EWAHConstants as EC

from ewah.hooks.base import EWAHBaseHook as BaseHook

from sshtunnel import SSHTunnelForwarder
from tempfile import NamedTemporaryFile
from datetime import timedelta
from pytz import timezone

import os

from typing import Optional, List, Dict, Any, Union


class EWAHSQLBaseOperator(EWAHBaseOperator):
    # Don't overwrite the _NAMES list to avoid accidentally exposing the SQL
    # base operator
    # _NAMES = []

    _ACCEPTED_EXTRACT_STRATEGIES = {
        EC.ES_FULL_REFRESH: True,
        EC.ES_INCREMENTAL: True,
    }

    def __init__(
        self,
        source_schema_name: Optional[str] = None,
        source_table_name: Optional[
            str
        ] = None,  # defaults to same as target_table_name
        source_database_name: Optional[str] = None,  # bigquery: project id
        sql_select_statement: Optional[str] = None,  # Alternative to specifying table
        timestamp_column: Optional[str] = None,
        where_clauses: Optional[Union[str, List[str]]] = None,
        extra_params: Optional[dict] = None,
        batch_size: int = 100000,
        *args,
        **kwargs
    ):
        source_table_name = source_table_name or kwargs["target_table_name"]
        super().__init__(*args, **kwargs)

        if isinstance(where_clauses, str):
            where_clauses = [where_clauses]

        if self.extract_strategy == EC.ES_INCREMENTAL:
            assert timestamp_column, "Incremental loading must have timestamp column!"

        if not sql_select_statement:
            assert source_schema_name
            assert source_table_name
            if self.columns_definition:
                columns_sql = "\n\t  {0}{1}{0}".format(
                    self._SQL_COLUMN_QUOTE,
                    "{0}\n\t, {0}".format(self._SQL_COLUMN_QUOTE).join(
                        self.columns_definition.keys()
                    ),
                )
            else:
                columns_sql = "*"
            sql_select_statement = self._SQL_BASE.format(
                columns=columns_sql,
                schema=source_schema_name,
                table=source_table_name,
                database=source_database_name,
            )

        self.sql = self._SQL_BASE_SELECT.format(select_sql=sql_select_statement)
        self.extra_params = extra_params
        self.timestamp_column = timestamp_column
        self.where_clauses = where_clauses
        self.batch_size = batch_size

    def ewah_execute(self, context):
        # called, potentially with a data_from and data_until

        params = self.extra_params or {}
        where_clauses = self.where_clauses or []
        if self.data_from:
            where_clauses.append(
                "{0} >= {1}".format(
                    self.timestamp_column, self._SQL_PARAMS.format("data_from")
                )
            )
            params["data_from"] = self.data_from
        if self.data_until:
            where_clauses.append(
                "{0} <= {1}".format(
                    self.timestamp_column, self._SQL_PARAMS.format("data_until")
                )
            )
            params["data_until"] = self.data_until

        where_clauses = where_clauses or ["1 = 1"]
        sql = self.sql.format("\n  AND ".join(where_clauses))
        for batch in self.source_hook.get_data_in_batches(
            sql=sql,
            params=params or None,  # Don't supply empty dict as params!
            return_dict=True,
            batch_size=self.batch_size,
        ):
            self.upload_data(batch)
