
from string import Template

import polars as pl

from database_sampler.files import get_settings
from database_sampler.conn import create_uri


# TODO: enable filtering
QUERY = Template("SELECT * FROM $entity_name")


def run(settings: str = "etc/settings.yml"):
    global_settings = get_settings(settings)

    for oper_name, oper_settings in global_settings["operations"].items():
        src_uri = create_uri(global_settings["connections"][oper_settings["origin"]])
        dst_uri = create_uri(global_settings["connections"][oper_settings["destination"]])

        for entity in oper_settings["entities"]:
            if "schema" in entity:
                full_name = f"{entity['schema']}.{entity['name']}"
            else:
                full_name = entity['name']

            # pulls data
            res = pl.read_database_uri(query=QUERY.substitute(entity_name=full_name), uri=src_uri, engine="adbc")

            # push data
            res.write_database(table_name=entity['name'], connection=dst_uri, engine="adbc")


if __name__ == "__main__":
    run()
