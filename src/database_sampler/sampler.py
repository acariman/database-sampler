from string import Template
from datetime import datetime

import polars as pl

from database_sampler.files import get_settings
from database_sampler.conn import create_uri


QUERY_ALL = Template("SELECT * FROM $name")
QUERY_FILTERED = Template("SELECT * FROM $name WHERE $column BETWEEN '$start' AND '$end'")


def execute(settings: str = "etc/settings.yml", start: datetime = None, end: datetime = None):
    global_settings = get_settings(settings)

    for oper_name, oper_settings in global_settings["operations"].items():
        src_uri = create_uri(global_settings["connections"][oper_settings["origin"]])
        dst_uri = create_uri(global_settings["connections"][oper_settings["destination"]])

        for entity in oper_settings["entities"]:
            entity["name"] = f"{entity['schema']}.{entity['name']}" if "schema" in entity else entity["name"]

            if "column" in entity:
                query = QUERY_FILTERED
                
                # TODO: enable different combinations
                # TODO: enable epoch timestamps
                entity["start"] = start 
                entity["end"] = end

            else:
                query = QUERY_ALL

            # pulls data
            res = pl.read_database_uri(query=query.substitute(entity), uri=src_uri, engine="adbc")

            # push data
            res.write_database(table_name=entity['name'], connection=dst_uri, engine="adbc")
