
from string import Template

import polars as pl

from database_sampler.files import get_settings
from database_sampler.conn import create_uri


# TODO: enable filtering
QUERY = Template("SELECT * FROM $entity_name")

def download(settings: str = "etc/settings.yml"):
    global_settings = get_settings(settings)

    for source_name, source_settings in global_settings["sources"].items():
        uri = create_uri(source_settings)

        for entity in source_settings["entities"]:
            if "schema" in entity:
                full_name = f"[{entity['schema']}].[{entity['name']}]"
            else:
                full_name = f"[{entity['name']}]"

            partial_res = pl.read_database_uri(query=QUERY.substitute(entity_name=full_name), uri=uri, engine="adbc")

            # TODO: saves data
