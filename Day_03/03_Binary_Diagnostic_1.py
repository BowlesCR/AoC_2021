import fileinput


def main() -> None:

    gamma = 0

    data = list(fileinput.input())
    bits = len(data[0]) - 1
    data = [int(d, 2) for d in data]

    p = 1 << bits - 1
    while p > 0:
        ones = [d for d in data if d & p]
        if len(ones) > 0.5 * len(data):
            gamma |= p
        p >>= 1

    epsilon = gamma ^ ((1 << bits) - 1)

    print(gamma, epsilon, gamma * epsilon)


if __name__ == "__main__":
    main()
