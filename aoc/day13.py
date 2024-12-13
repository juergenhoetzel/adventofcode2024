import re
import sys
from dataclasses import dataclass
from itertools import batched
from pathlib import Path

NUMBERS_RE = re.compile(r"\d")


@dataclass
class Machine:
    a0: int
    a1: int
    b0: int
    b1: int
    r0: int
    r1: int


def gauss(m: Machine) -> Machine:
    if m.a1:
        return Machine(m.a0, 0, m.b0, m.b1 * m.a0 - m.b0 * m.a1, m.r0, m.r1 * m.a0 - m.r0 * m.a1)
    return m


def parse_machines(s: str) -> list[Machine]:
    return [gauss(Machine(*xs)) for xs in batched((int(s) for s in re.findall(r"\d+", s)), n=6)]


def valid_buttons(m: Machine) -> None | tuple[int, int]:
    assert m.a1 == 0
    b, r = divmod(m.r1, m.b1)
    if r == 0:
        a, r = divmod((m.r0 - b * m.b0), m.a0)
        if r == 0:
            return a, b


def part1(ms: list[Machine]) -> int:
    return sum(bs[0] * 3 + bs[1] for m in ms if (bs := valid_buttons(m)))


def main():
    machines = parse_machines(Path(sys.argv[1]).read_text())
    print(f"Part 1: {part1(machines)}")


if __name__ == "__main__":
    main()
