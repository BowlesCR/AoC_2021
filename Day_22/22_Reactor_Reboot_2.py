import fileinput
import re

Cube = tuple[str, int, int, int, int, int, int]


def overlap(self: Cube, cubes: list[Cube]):
    # Heavily inspired by https://www.reddit.com/r/adventofcode/comments/rlxhmg/comment/hpl5o4v/?utm_source=share&utm_medium=web2x&context=3
    a, x1, x2, y1, y2, z1, z2 = self

    assert x1 <= x2 and y1 <= y2 and z1 <= z2, "Ordering violation"

    negates = []

    for oa, ox1, ox2, oy1, oy2, oz1, oz2 in cubes:
        if ox2 < x1 or x2 < ox1 or oy2 < y1 or y2 < oy1 or oz2 < z1 or z2 < oz1:
            continue

        cx1 = max(x1, ox1)
        cx2 = min(x2, ox2)
        cy1 = max(y1, oy1)
        cy2 = min(y2, oy2)
        cz1 = max(z1, oz1)
        cz2 = min(z2, oz2)

        # Subtract -- these are either double-counted or off
        negates.append((-1 * oa, cx1, cx2, cy1, cy2, cz1, cz2))
    if a == 1:
        cubes.append(self)

    cubes.extend(negates)


def main():
    cubes: list[Cube] = []

    reg = re.compile(
        r"(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)"
    )
    for m in [reg.match(line) for line in fileinput.input()]:
        a = 1 if m.group(1) == "on" else 0
        overlap((a, *map(int, m.groups()[1:])), cubes)

    count = 0
    for a, x1, x2, y1, y2, z1, z2 in cubes:
        if not a:
            continue
        count += a * (abs(x2 - x1 + 1) * abs(y2 - y1 + 1) * abs(z2 - z1 + 1))
    print(count)


if __name__ == "__main__":
    main()
