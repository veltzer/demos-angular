from typing import List


config_requires: List[str] = [
    "pyclassifiers",
]
dev_requires: List[str] = []
install_requires: List[str] = []
build_requires: List[str] = [
    "pymakehelper",
    "pydmt",
    "pyclassifiers",
]
test_requires: List[str] = []
requires = config_requires + install_requires + build_requires + test_requires
