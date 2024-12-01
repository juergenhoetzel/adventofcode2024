from pathlib import Path

import pytest
from aoc.day1 import day1

TESTDATA = """
3   4
4   3
2   5
1   3
3   9
3   3
"""


@pytest.fixture(scope="session")
def input_path(tmpdir_factory):
    p = Path(tmpdir_factory.mktemp("data")) / "input.txt"
    p.write_text(TESTDATA)
    return p


def test_day1(input_path):
    assert day1(input_path) == 11
