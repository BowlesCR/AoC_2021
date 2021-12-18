import fileinput

grid: list[list[int]]
risks: dict[tuple[int, int], int]


def updateRisk(node: tuple[int, int]) -> None:
    r, c = node

    risk = min(
        [
            risks.get((r - 1, c), 999999) + grid[r][c],
            risks.get((r + 1, c), 999999) + grid[r][c],
            risks.get((r, c - 1), 999999) + grid[r][c],
            risks.get((r, c + 1), 999999) + grid[r][c],
            risks.get(node),
        ]
    )

    risks[node] = risk


def main() -> None:
    global grid, risks
    grid = [[int(i) for i in line.strip()] for line in fileinput.input()]

    unvisited: set[tuple[int, int]] = set()

    # Initialize risks
    risks = {}
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            risks[(r, c)] = 999999
            unvisited.add((r, c))
    risks[(0, 0)] = 0

    target = (len(grid) - 1, len(grid[0]) - 1)

    while target in unvisited:
        current = None
        min_risk = 999999
        for n in unvisited:
            if risks[n] < min_risk:
                min_risk = risks[n]
                current = n
        del min_risk

        r, c = current

        if r > 0 and (r - 1, c) in unvisited:
            updateRisk((r - 1, c))
        if r < len(grid) - 1 and (r + 1, c) in unvisited:
            updateRisk((r + 1, c))
        if c > 0 and (r, c - 1) in unvisited:
            updateRisk((r, c - 1))
        if c < len(grid[0]) - 1 and (r, c + 1) in unvisited:
            updateRisk((r, c + 1))

        unvisited.remove(current)

    print(risks[target])


if __name__ == "__main__":
    main()
