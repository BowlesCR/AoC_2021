import fileinput


def main() -> None:

    h = d = 0

    for s in fileinput.input():
        (op, mag) = s.split()
        mag = int(mag)
        if op == "forward":
            h += mag
        elif op == "down":
            d += mag
        elif op == "up":
            d -= mag

    print(h*d)


if __name__ == "__main__":
    main()
