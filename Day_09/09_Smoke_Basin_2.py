import fileinput
from math import prod


def main() -> None:

    grid: list[list[int]] = [
        [int(i) for i in line.strip()] for line in fileinput.input()
    ]

    sizes: list[int] = []

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            h = grid[r][c]
            if r > 0:
                if grid[r - 1][c] <= h:
                    continue
            if r < len(grid) - 1:
                if grid[r + 1][c] <= h:
                    continue
            if c > 0:
                if grid[r][c - 1] <= h:
                    continue
            if c < len(grid[r]) - 1:
                if grid[r][c + 1] <= h:
                    continue

            sizes.append(check(grid, r, c))

    print(prod(sorted(sizes)[-3:]))


def check(grid: list[list[int]], r: int, c: int) -> int:
    if grid[r][c] == 9:
        return 0

    count = 1  # Count current loc
    grid[r][c] = 9  # Route poison

    if r > 0:
        count += check(grid, r - 1, c)
    if r < len(grid) - 1:
        count += check(grid, r + 1, c)
    if c > 0:
        count += check(grid, r, c - 1)
    if c < len(grid[r]) - 1:
        count += check(grid, r, c + 1)

    return count


if __name__ == "__main__":
    main()
