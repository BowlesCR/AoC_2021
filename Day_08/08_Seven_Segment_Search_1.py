import fileinput


def main() -> None:

    acc = 0

    line: str
    for line in fileinput.input():
        line.strip()
        line = line.split("|")

        out = line[1].split()

        acc += len([o for o in out if len(o) in [2, 3, 4, 7]])

    print(acc)


if __name__ == "__main__":
    main()
