
import pytest

from database_sampler.files import get_settings

def test_get_settings():
    res = get_settings()
    print(res)

    assert "connections" in res
    assert "sqlite" in res["connections"]["sample"]["driver"]
    assert "files/res.sqlite" in res["connections"]["result"]["file"]

    assert "operations" in res
    assert "entities" in res["operations"]["sqlite2sqlite"]
    assert "sample" in res["operations"]["sqlite2sqlite"]["origin"]
    assert "Album" in res["operations"]["sqlite2sqlite"]["entities"][0]["name"]
    
