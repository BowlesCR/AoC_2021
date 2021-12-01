import fileinput


def main() -> None:
    scans = [int(s) for s in fileinput.input()]
    count = 0
    for i in range(1, len(scans)):
        if scans[i] > scans[i - 1]:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
