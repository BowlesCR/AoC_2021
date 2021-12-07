import fileinput
import statistics


def main() -> None:
    crabs = [int(f) for f in list(fileinput.input())[0].split(",")]
    median = statistics.median(crabs)

    print(sum([abs(c - median) for c in crabs]))


if __name__ == "__main__":
    main()
