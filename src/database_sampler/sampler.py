import logging
from string import Template
from datetime import datetime

import polars as pl
import typer

from database_sampler.files import get_settings
from database_sampler.conn import create_uri


app = typer.Typer()

QUERY_ALL = Template("SELECT * FROM $name")
QUERY_FILTERED = Template(
    "SELECT * FROM $name WHERE $column BETWEEN '$start' AND '$end'"
)


@app.command()
def execute(
    settings: str = "etc/settings.yml", start: datetime = None, end: datetime = None
):
    global_settings = get_settings(settings)

    for oper_name, oper_settings in global_settings["operations"].items():
        logging.info(
            f"Running {oper_name} operation ('{oper_settings['origin']}' -> '{oper_settings['destination']}')"
        )

        src_uri = create_uri(global_settings["connections"][oper_settings["origin"]])
        dst_uri = create_uri(
            global_settings["connections"][oper_settings["destination"]]
        )

        for entity in oper_settings["entities"]:
            logging.info(f"Working on '{entity['name']}'")
            entity["name"] = (
                f"{entity['schema']}.{entity['name']}"
                if "schema" in entity
                else entity["name"]
            )

            if "column" in entity:
                logging.debug("Will fetch filtered data")
                query = QUERY_FILTERED

                # TODO: enable different combinations
                # TODO: enable epoch timestamps
                entity["start"] = start
                entity["end"] = end

            else:
                logging.debug("Will fetch all data")
                query = QUERY_ALL

            # pulls data
            logging.debug("Origin fetching")
            res = pl.read_database_uri(
                query=query.substitute(entity), uri=src_uri, engine="adbc"
            )

            # push data
            logging.debug("Destination writing")
            res.write_database(
                table_name=entity["name"], connection=dst_uri, engine="adbc"
            )
