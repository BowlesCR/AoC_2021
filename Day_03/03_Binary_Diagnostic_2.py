import fileinput


def main() -> None:
    data = list(fileinput.input())
    bits = len(data[0]) - 1
    data = {int(d, 2) for d in data}

    ox = co = data
    p = 1 << bits - 1
    while p > 0 and (len(ox) > 1 or len(co) > 1):
        if len(ox) > 1:
            ones = {d for d in ox if d & p}
            if len(ones) >= 0.5 * len(ox):
                ox = ones
            else:
                ox = ox.difference(ones)
        if len(co) > 1:
            ones = {d for d in co if d & p}
            if len(ones) < 0.5 * len(co):
                co = ones
            else:
                co = co.difference(ones)

        p >>= 1

    ox = ox.pop()
    co = co.pop()

    print(ox, co, ox * co)


if __name__ == "__main__":
    main()
