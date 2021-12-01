import fileinput


def main() -> None:
    scans = [int(s) for s in fileinput.input()]
    count = 0
    for i in range(3, len(scans)):
        this = scans[i - 2 : i + 1]
        last = scans[i - 3 : i]
        if sum(this) > sum(last):
            count += 1

    print(count)


if __name__ == "__main__":
    main()
