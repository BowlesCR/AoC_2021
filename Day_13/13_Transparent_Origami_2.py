import fileinput
import re


def main() -> None:

    coords: set[tuple[int, int]] = set()

    line: str
    for line in fileinput.input():
        if line == "\n":
            continue
        elif line.startswith("fold along"):
            m = re.match(r"fold along (.)=(\d+)\n?", line)
            fold = int(m.group(2))
            if m.group(1) == "y":
                for c in [c for c in coords if c[0] >= fold]:
                    assert c[0] != fold
                    new_r = fold - (c[0] - fold)
                    coords.remove(c)
                    coords.add((new_r, c[1]))
            elif m.group(1) == "x":
                for c in [c for c in coords if c[1] >= fold]:
                    assert c[1] != fold
                    new_c = fold - (c[1] - fold)
                    coords.remove(c)
                    coords.add((c[0], new_c))
        else:
            c, r = line.strip().split(",")
            coords.add((int(r), int(c)))

    max_r = max([c[0] for c in coords])
    max_c = max([c[1] for c in coords])

    grid: list[list[str]] = []
    for r in range(max_r + 1):
        grid.append([" "] * (max_c + 1))

    for c in coords:
        grid[c[0]][c[1]] = "█"

    for r in grid:
        print("".join(r))


if __name__ == "__main__":
    main()
