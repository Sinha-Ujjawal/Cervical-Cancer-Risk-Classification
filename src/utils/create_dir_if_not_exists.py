import os
from typing import Optional


def create_dir_if_not_exists(dirpath: str) -> Optional[bool]:
    """This helper function is for making dirs if it does not exists

    Args:
        dirpath (str): [the path of the directory]

    Returns:
        Optional[bool]: [True if a directory is created else None]
    """
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)
