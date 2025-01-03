import operator
import re
import sys
from pathlib import Path
from typing import Generator

STATE_RE = re.compile(r"^([\w]+): ([\d])+$")
INS_RE = re.compile(r"^([\w]+) (AND|XOR|OR) ([\w]+) -> ([\w]+)$")


def parse_input(s: str) -> tuple[dict[str, bool | None], list[tuple[str, str, str, str]]]:
    state_s, ins_s = tuple(s.split("\n\n"))
    state = dict()
    ins = []
    for line in state_s.splitlines():
        assert (m := STATE_RE.match(line))
        state[m.group(1)] = bool(int(m.group(2)))
    for line in ins_s.splitlines():
        assert (m := INS_RE.match(line))
        ins.append(m.groups())
    return state, ins


def update_list(d: dict[str, bool | None], ins_list: list[tuple[str, str, str, str]]):
    ins_set = set(ins_list)
    while ins_set:
        for ins in ins_list:
            left, op_s, right, target = ins
            match op_s:
                case "OR":
                    op = operator.__or__
                case "AND":
                    op = operator.__and__
                case "XOR":
                    op = operator.__xor__
                case _:
                    raise ValueError("Invalid Binop")
            if not target in d and left in d and right in d:
                d[target] = op(d[left], d[right])
                ins_set.remove(ins)


def part1(d, ins_list):
    update_list(d, ins_list)
    return sum([v * (2 ** int(k[1:])) for (k, v) in d.items() if k.startswith("z")])


IN_OUT_REGS = {"x", "y", "z"}


def wrong_ops(ins_list: list[tuple[str, str, str, str]]) -> Generator[str, None, None]:
    for op1, op, op2, opout in ins_list:
        if (
            opout[0] == "z"
            and op != "XOR"
            and opout != "z45"
            or (op == "XOR" and opout[0] not in IN_OUT_REGS and op1[0] not in IN_OUT_REGS and op2[0] not in IN_OUT_REGS)
        ):
            yield opout
        if op == "AND" and "x00" not in [op1, op2]:
            for sop1, subop, subop2, _ in ins_list:
                if (opout == sop1 or opout == subop2) and subop != "OR":
                    yield (opout)
        if op == "XOR":
            for sop1, subop, subop2, _ in ins_list:
                if (opout == sop1 or opout == subop2) and subop == "OR":
                    yield (opout)


def part2(ins_list):
    to_switch = sorted(set(wrong_ops(ins_list)))
    return ",".join(to_switch)


def main():
    d, ins_list = parse_input(Path(sys.argv[1]).read_text())
    print(f"Part 1: {part1(d, ins_list)}")

    print(f"Part 2: {part2(ins_list)}")


if __name__ == "__main__":
    main()
