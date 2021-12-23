import fileinput
import itertools
import re


def main():
    cubes: dict[tuple[int, int, int], bool] = {}

    reg = re.compile(
        r"(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)"
    )
    for m in [reg.match(line) for line in fileinput.input()]:
        action = m.group(1)
        x1 = int(m.group(2))
        x2 = int(m.group(3))
        y1 = int(m.group(4))
        y2 = int(m.group(5))
        z1 = int(m.group(6))
        z2 = int(m.group(7))

        if not ((-50 <= x1 <= 50) and (-50 <= y1 <= 50) and (-50 <= z1 <= 50)):
            continue

        for t in itertools.product(
            range(x1, x2 + 1), range(y1, y2 + 1), range(z1, z2 + 1)
        ):
            cubes[t] = action == "on"

    print(len([i for i in cubes.items() if i[1]]))


if __name__ == "__main__":
    main()
