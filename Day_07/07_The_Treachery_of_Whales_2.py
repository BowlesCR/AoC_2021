import fileinput
import statistics


def main() -> None:
    crabs = [int(f) for f in list(fileinput.input())[0].split(",")]
    mean = statistics.mean(crabs)

    # Problem data requires truncation
    mean_trunc = int(mean)
    fuel1 = 0
    for c in crabs:
        for d in range(1, abs(c - mean_trunc) + 1):
            fuel1 += d

    # Sample data requires proper rounding
    mean_round = round(mean)
    fuel2 = 0
    for c in crabs:
        for d in range(1, abs(c - mean_round) + 1):
            fuel2 += d

    print(min(fuel1, fuel2))


if __name__ == "__main__":
    main()
