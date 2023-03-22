import pytest

from utils import dicts


@pytest.mark.parametrize("collection, key, expected_result", [({"vcs": "mercurial"}, "vcs", "mercurial"),
                                                              ({}, 2, "git"),
                                                              ({"American Idiot": "Holiday"}, "Peacemaker", "git"),
                                                              ])
def test_get_val(collection, key, expected_result):
    assert dicts.get_val(collection, key) == expected_result


def test_get_val_change_default():
    assert dicts.get_val({"American Idiot": "Holiday"}, "21 Guns", "Another album") == "Another album"
