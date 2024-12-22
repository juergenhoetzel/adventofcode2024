import sys
from pathlib import Path


def next_secret(secret):
    secret = ((secret * 64) ^ secret) % 16777216
    secret = ((secret // 32) ^ secret) % 16777216
    secret = ((secret * 2048) ^ secret) % 16777216
    return secret


def gen_n_secret(secret, n):
    for _ in range(n):
        secret = next_secret(secret)
    return secret


def parse_input(s: str):
    return [int(line) for line in s.splitlines()]


def part1(xs: list[int]):
    return sum(gen_n_secret(x, 2000) for x in xs)


def main():
    xs = parse_input(Path(sys.argv[1]).read_text())
    print(f"Part1: {part1(xs)}")


if __name__ == "__main__":
    main()
