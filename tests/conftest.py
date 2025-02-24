import sqlite3
from os import chdir, remove
from pathlib import Path

import httpx
import pytest


DB_URL = "https://raw.githubusercontent.com/lerocha/chinook-database/master/ChinookDatabase/DataSources/Chinook_Sqlite.sqlite"
DB_PATH = "files/database.sqlite"
RES_PATH = "files/res.sqlite"


# when running tests, moves to
if Path("./tests/").exists():
    chdir("./tests/")


def download_database(url: str, output_path: str) -> None:
    """
    Download a database from a URL and save it locally.

    Parameters
    ----------
    url : str
        URL of the database to download.
    output_path : str
        Path where the database will be saved.
    """
    with httpx.stream("GET", url) as response:
        response.raise_for_status()
        with open(output_path, "wb") as file:
            for chunk in response.iter_bytes(chunk_size=8192):
                file.write(chunk)


def clean():
    """
    Cleans result from previous tests.
    """
    path = Path(RES_PATH)

    if path.exists():
        remove(RES_PATH)


@pytest.fixture()
def setup_database():
    """
    Download and prepare the database for testing.
    """
    path = Path(DB_PATH)

    if not path.parent.exists():
        path.parent.mkdir()

    if not path.exists():
        download_database(DB_URL, DB_PATH)

    clean()

    # Checks file
    connection = sqlite3.connect(DB_PATH)
    yield connection
    connection.close()
