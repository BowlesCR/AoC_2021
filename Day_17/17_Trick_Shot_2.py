import fileinput
import re


def main() -> None:
    for line in fileinput.input():

        m = re.search(r"x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)$", line)
        del line

        x_min = int(m.group(1))
        x_max = int(m.group(2))
        y_min = int(m.group(3))
        y_max = int(m.group(4))

        del m

        solutions: set[tuple[int, int]] = set()
        h_max = 0
        for x_v_i in range(1, x_max + 1):
            for y_v_i in range(y_min, 1000):
                maxheight = 0
                x = y = 0
                x_v = x_v_i
                y_v = y_v_i
                while x <= x_max and y >= y_min:
                    x += x_v
                    y += y_v
                    x_v = max(0, x_v - 1)
                    y_v -= 1
                    maxheight = max(y, maxheight)

                    if x_min <= x <= x_max and y_min <= y <= y_max:
                        solutions.add((x_v_i, y_v_i))
                        h_max = max(h_max, maxheight)
                        break

        print(h_max)
        print(len(solutions))


if __name__ == "__main__":
    main()
