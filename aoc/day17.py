import sys
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Computer:
    program: list[int]
    a: int
    b: int
    c: int
    ip: int = 0
    output: list[int] = field(default_factory=list)

    def combo_val(self, c):
        match c:
            case 4:
                return self.a
            case 5:
                return self.b
            case 6:
                return self.c
            case _:
                return c

    def step(self) -> bool:
        i = self.program[self.ip]
        o = self.program[self.ip + 1]
        self.ip += 2
        match i:
            case 0:
                self.a = self.a // (2 ** self.combo_val(o))
            case 1:
                self.b = self.b ^ o
            case 2:
                self.b = self.combo_val(o) % 8
            case 3:
                if self.a != 0:
                    self.ip = o
            case 4:
                self.b = self.b ^ self.c
            case 5:
                self.output.append(self.combo_val(o) % 8)
            case 6:
                self.b = self.a // (2 ** self.combo_val(o))
            case 7:
                self.c = self.a // (2 ** self.combo_val(o))
        return self.ip < len(self.program)


def parse_input(s: str) -> Computer:
    [a, b, c, _, prog] = s.splitlines()
    return Computer(
        [int(c) for c in prog.removeprefix("Program: ").split(",")],
        int(a.removeprefix("Register A: ")),
        int(b.removeprefix("Register B: ")),
        int(c.removeprefix("Register C: ")),
    )


def part1(c: Computer) -> str:
    while c.step():
        ...
    return ",".join((str(i) for i in c.output))


def search_regs(comp: Computer, a=0, prg_pos=-1):
    if abs(prg_pos) > len(comp.program):
        return a
    for i in range(8):
        comp.ip = 0
        comp.output = []
        comp.a = a * 8 + i
        while comp.step():
            ...
        if comp.output[0] == comp.program[prg_pos]:
            if ar := search_regs(comp, a * 8 + i, prg_pos - 1):
                return ar


def part2(comp: Computer):
    return search_regs(comp)


def main():
    c = parse_input(Path(sys.argv[1]).read_text())
    print(f"Part1: {part1(c)}")
    print(f"Part1: {part2(c)}")


if __name__ == "__main__":
    main()
