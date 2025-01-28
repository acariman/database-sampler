
import pytest

from database_sampler.files import get_settings

def test_get_settings():
    res = get_settings()
    print(res)

    assert "connection" in res["sources"]["test"]
    assert "entities" in res["sources"]["test"]
    assert "sqlite" in res["sources"]["test"]["connection"]["driver"]
