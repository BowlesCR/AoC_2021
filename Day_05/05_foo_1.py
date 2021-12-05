import fileinput
import re


def main() -> None:

    SIZE = 1000

    r = re.compile(r"^(\d+),(\d+) -> (\d+),(\d+)$")

    lines: list[tuple[str]] = [r.match(line).groups() for line in fileinput.input()]

    grid: list[list[int]] = []
    for r in range(SIZE):
        grid.append([0] * SIZE)

    for line in lines:
        x = sorted([int(line[0]), int(line[2])])
        y = sorted([int(line[1]), int(line[3])])

        if x[0] == x[1] or y[0] == y[1]:
            # Horizontal/Vertical
            for c in range(x[0], x[1] + 1):
                for r in range(y[0], y[1] + 1):
                    grid[r][c] += 1

    count = 0
    for r in grid:
        count += len([c for c in r if c > 1])

    print(count)


if __name__ == "__main__":
    main()
