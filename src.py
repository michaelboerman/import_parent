import os
import sys
import inspect
from typing import Union


def _get_caller_dir(stack_level: int = 2) -> str:
    frame = inspect.stack()[stack_level]
    caller_file = frame.filename
    return os.path.dirname(os.path.abspath(caller_file))


def _count_levels(path: str) -> int:
    parts = [p for p in path.replace("\\", "/").split("/") if p]
    levels = sum(1 for p in parts if p == "..")

    if levels == 0:
        raise ValueError("Path must contain at least one '..'")

    return levels


def import_parent(path: Union[str, int] = "..") -> str:
    """
    Add a parent directory (relative to the caller) to sys.path.

    Parameters
    ----------
    path : str or int
        '../..' style path or an integer number of levels.

    Returns
    -------
    str
        The directory added to sys.path
    """
    if isinstance(path, int):
        if path <= 0:
            raise ValueError("Integer path must be > 0")
        levels_up = path
    elif isinstance(path, str):
        levels_up = _count_levels(path)
    else:
        raise TypeError("path must be a string or int")

    caller_dir = _get_caller_dir()

    target_dir = caller_dir
    for _ in range(levels_up):
        target_dir = os.path.dirname(target_dir)

    if not os.path.isdir(target_dir):
        raise FileNotFoundError(f"Resolved path does not exist: {target_dir}")

    if target_dir not in sys.path:
        sys.path.insert(0, target_dir)

    return target_dir
