import itertools
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


def price_generator(secret):
    secrets = [secret % 10]
    for _ in range(2000):
        secret = next_secret(secret)
        secrets.append(secret % 10)
    return secrets


def part2(xs: list[int]):
    acc = dict()
    prices_lists = [price_generator(x) for x in xs]
    for prices in prices_lists:
        p_diffs = [x1 - x2 for x1, x2 in itertools.pairwise(prices)]
        seen = set()
        for i in range(len(p_diffs) - 3):
            if (k := tuple(p_diffs[i : i + 4])) not in seen:
                seen.add(k)
                acc[k] = acc.get(k, 0) + prices[i + 4]
    return max(acc.values())


def main():
    xs = parse_input(Path(sys.argv[1]).read_text())
    print(f"Part1: {part1(xs)}")
    print(f"Part1: {part2(xs)}")


if __name__ == "__main__":
    main()
