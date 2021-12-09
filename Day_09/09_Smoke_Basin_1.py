import fileinput


def main() -> None:

    grid: list[list[int]] = [
        [int(i) for i in line.strip()] for line in fileinput.input()
    ]

    risk = 0

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

            risk += 1 + h

    print(risk)


if __name__ == "__main__":
    main()
