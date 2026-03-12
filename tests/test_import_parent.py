import sys
import os
from import_parent import add_parent_to_path


def test_integer_levels_adds_path():
    original_sys_path = sys.path.copy()

    try:
        added = add_parent_to_path(1)
        assert isinstance(added, str)
        assert added in sys.path
    finally:
        sys.path[:] = original_sys_path


def test_string_levels_adds_path():
    original_sys_path = sys.path.copy()

    try:
        added = add_parent_to_path("../")
        assert isinstance(added, str)
        assert added in sys.path
    finally:
        sys.path[:] = original_sys_path


def test_idempotent_behavior():
    original_sys_path = sys.path.copy()

    try:
        path1 = add_parent_to_path(1)
        path2 = add_parent_to_path(1)

        assert path1 == path2
        assert sys.path.count(path1) == 1
    finally:
        sys.path[:] = original_sys_path


def test_invalid_integer_raises():
    try:
        add_parent_to_path(0)
    except ValueError:
        assert True
    else:
        assert False


def test_invalid_string_raises():
    try:
        add_parent_to_path("not/a/parent/path")
    except ValueError:
        assert True
    else:
        assert False


def test_resolved_path_exists():
    added = add_parent_to_path(1)
    assert os.path.isdir(added)
