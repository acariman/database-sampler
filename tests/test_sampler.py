
from database_sampler.sampler import download


def test_download(setup_database):
    download()
