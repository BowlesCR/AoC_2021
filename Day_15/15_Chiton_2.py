import fileinput

grid: list[list[int]]
risks: dict[tuple[int, int], int]

INF: int = 999999


def updateRisk(node: tuple[int, int]) -> None:
    r, c = node

    risk = min(
        [
            risks[n] + grid[r][c]
            for n in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1))
            if n in risks
        ]
    )

    risks[node] = risk


def calcGrid(node: tuple[int, int]) -> int:
    r, c = node
    dim = len(grid)

    offset = (r // dim) + (c // dim)
    risk = grid[r % dim][c % dim]
    for i in range(offset):
        if risk == 9:
            risk = 1
        else:
            risk += 1
    return risk


def main() -> None:
    global grid, risks
    grid = [[int(i) for i in line.strip()] for line in fileinput.input()]

    dim = len(grid)

    grid = [[calcGrid((r, c)) for c in range(dim * 5)] for r in range(dim * 5)]

    unvisited: set[tuple[int, int]] = set()
    candidates: set[tuple[int, int]] = {(0, 0)}

    # Initialize risks
    risks = {(0, 0): 0}

    for r in range(dim * 5):
        for c in range(dim * 5):
            unvisited.add((r, c))

    target = (dim * 5 - 1, dim * 5 - 1)

    while target in unvisited:
        if len(unvisited) % 1000 == 0:
            print(f"Candidates, Unvisted: {len(candidates)}, {len(unvisited)}")

        current = min(candidates, key=lambda n: risks[n])

        r, c = current

        tup = (r - 1, c)
        if r > 0 and tup in unvisited:
            updateRisk(tup)
            candidates.add(tup)

        tup = (r + 1, c)
        if r < dim * 5 - 1 and tup in unvisited:
            updateRisk(tup)
            candidates.add(tup)

        tup = (r, c - 1)
        if c > 0 and tup in unvisited:
            updateRisk(tup)
            candidates.add(tup)

        tup = (r, c + 1)
        if c < dim * 5 - 1 and tup in unvisited:
            updateRisk(tup)
            candidates.add(tup)
        del tup

        unvisited.remove(current)
        candidates.remove(current)

    print(risks[target])


if __name__ == "__main__":
    main()
