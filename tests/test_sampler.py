from datetime import datetime

from database_sampler.sampler import execute


def test_download(setup_database):
    start = datetime(2009, 1, 1)
    end = datetime(2009, 1, 30)

    execute(start=start, end=end)
