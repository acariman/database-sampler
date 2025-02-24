from datetime import datetime

import polars as pl

from database_sampler.sampler import execute, QUERY_ALL
from database_sampler.files import get_settings
from database_sampler.conn import create_uri


def _query_result(uri, table):
    return pl.read_database_uri(
        query=QUERY_ALL.substitute(name=table), uri=uri, engine="adbc"
    )


def test_download(setup_database):
    start = datetime(2009, 1, 1)
    end = datetime(2009, 1, 30)

    execute(start=start, end=end)

    global_settings = get_settings()
    dst_uri = create_uri(global_settings["connections"]["result"])

    res_full = _query_result(dst_uri, "Album")
    assert len(res_full) == 347

    res_filtered = _query_result(dst_uri, "Invoice")
    assert len(res_filtered) == 6
    assert datetime.fromisoformat(min(res_filtered["InvoiceDate"])) >= start
    assert datetime.fromisoformat(max(res_filtered["InvoiceDate"])) <= end
