import sys
from pathlib import Path


def parse_input(s: str) -> list[int]:
    is_block = True
    current_id = 0
    current_pos = 0
    blocks = []
    for b in s:
        length = int(b)
        if is_block:
            blocks += [current_id] * length
            current_id += 1
        else:
            blocks += [None] * length
        is_block = not is_block  # alternate
        current_pos += length
    return blocks


def relocate(blocks: list[int]):
    for i in range(len(blocks) - 1, 0, -1):
        if blocks[i]:
            for j in range(i):
                if blocks[j] is None:
                    blocks[i], blocks[j] = blocks[j], blocks[i]
                    return True
    return False


def checksum(blocks) -> int:
    return sum([i * x for i, x in enumerate(blocks) if x])


def part1(blocks):
    while relocate(blocks):
        ...
    return checksum(blocks)


def main():
    blocks = parse_input(Path(sys.argv[1]).read_text().splitlines()[0])
    print(f"Part 1: {part1(blocks)}")


if __name__ == "__main__":
    main()
