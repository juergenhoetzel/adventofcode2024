from pathlib import Path

import pytest

from aoc.day2 import count_report_safe, is_safe, is_safe_dampened

TESTDATA = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


def test_day2_is_safe():
    assert is_safe([7, 6, 4, 2, 1])
    assert not is_safe([1, 2, 7, 8, 9])
    assert not is_safe([9, 7, 6, 2, 1])
    assert not is_safe([1, 3, 2, 4, 5])
    assert not is_safe([8, 6, 4, 4, 1])
    assert is_safe([1, 3, 6, 7, 9])


@pytest.fixture(scope="session")
def input_path(tmpdir_factory):
    p = Path(tmpdir_factory.mktemp("data")) / "input.txt"
    p.write_text(TESTDATA)
    return p


def test_day2_count_reports(input_path):
    assert count_report_safe(input_path) == 2


def test_day2_is_dampened_safe():
    assert is_safe_dampened([7, 6, 4, 2, 1])
    assert not is_safe_dampened([1, 2, 7, 8, 9])
    assert not is_safe_dampened([9, 7, 6, 2, 1])
    assert is_safe_dampened([1, 3, 2, 4, 5])
    assert is_safe_dampened([8, 6, 4, 4, 1])
    assert is_safe_dampened([1, 3, 6, 7, 9])


def test_day2_count_dampened_reports(input_path):
    assert count_report_safe(input_path, is_safe_fn=is_safe_dampened) == 4
