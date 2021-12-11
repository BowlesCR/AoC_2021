import fileinput


def main() -> None:
    grid: list[list[int]] = [
        [int(i) for i in line.strip()] for line in fileinput.input()
    ]

    flashes = 0
    for s in range(100):

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                grid[r][c] += 1

        loop = True
        while loop:
            loop = False

            for r in range(len(grid)):
                for c in range(len(grid[r])):
                    if grid[r][c] > 9:
                        flashes += 1
                        grid[r][c] = -1  # Poison

                        for r1 in range(r - 1, r + 2):
                            if r1 < 0 or r1 >= len(grid):
                                continue
                            for c1 in range(c - 1, c + 2):
                                if c1 < 0 or c1 >= len(grid[r1]):
                                    continue

                                if grid[r1][c1] != -1:
                                    grid[r1][c1] += 1
                                    loop = True

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] < 0:
                    grid[r][c] = 0

        print(s + 1, flashes)


if __name__ == "__main__":
    main()
