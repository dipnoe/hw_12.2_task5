import pytest

from utils import dicts


@pytest.mark.parametrize("collection, key, expected_result", [({"vcs": "mercurial"}, "vcs", "mercurial"),
                                                              ({}, 2, "git"),
                                                              ({"American Idiot": "Holiday"}, "Peacemaker", "git"),
                                                              ])
def test_get_val(collection, key, expected_result):
    assert dicts.get_val(collection, key) == expected_result
