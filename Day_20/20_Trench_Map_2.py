import fileinput
from functools import lru_cache

alg: list[str]
inp: dict[tuple[int, int], str]


@lru_cache(maxsize=None)
def get(pos: tuple[int, int], layer: int = 0) -> str:
    r, c = pos
    if layer == 0:
        num = (
            inp.get((r - 1, c - 1), "0"),
            inp.get((r - 1, c), "0"),
            inp.get((r - 1, c + 1), "0"),
            inp.get((r, c - 1), "0"),
            inp.get((r, c), "0"),
            inp.get((r, c + 1), "0"),
            inp.get((r + 1, c - 1), "0"),
            inp.get((r + 1, c), "0"),
            inp.get((r + 1, c + 1), "0"),
        )
    else:
        num = (
            get((r - 1, c - 1), layer - 1),
            get((r - 1, c), layer - 1),
            get((r - 1, c + 1), layer - 1),
            get((r, c - 1), layer - 1),
            get((r, c), layer - 1),
            get((r, c + 1), layer - 1),
            get((r + 1, c - 1), layer - 1),
            get((r + 1, c), layer - 1),
            get((r + 1, c + 1), layer - 1),
        )

    num = int("".join(num), 2)

    if alg[num] == "#":
        return "1"
    else:
        return "0"


def main() -> None:
    global alg, inp
    lines = [line.strip() for line in fileinput.input()]

    alg = lines[0]

    dim = len(lines) - 2
    inp = {}
    for r in range(2, len(lines)):
        for c in range(len(lines[r])):
            if lines[r][c] == "#":
                inp[(r - 2, c)] = "1"
            # Don't bother storing the 0's, we're just going to imply it later

    del lines

    DEPTH = 50
    out: set[tuple[int, int]] = set()
    for r in range(-DEPTH, dim + DEPTH):
        for c in range(-DEPTH, dim + DEPTH):

            p = get((r, c), DEPTH - 1)
            if p == "1":
                out.add((r, c))

    print(len(out))


if __name__ == "__main__":
    main()
