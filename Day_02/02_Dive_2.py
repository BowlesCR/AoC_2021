import fileinput


def main() -> None:

    h = d = a = 0

    for s in fileinput.input():
        (op, mag) = s.split()
        mag = int(mag)
        if op == "forward":
            h += mag
            d += (a * mag)
        elif op == "down":
            a += mag
        elif op == "up":
            a -= mag

    print(h*d)


if __name__ == "__main__":
    main()
