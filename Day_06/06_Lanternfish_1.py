import fileinput
from collections import Counter

DAYS = 256


def main() -> None:
    state: Counter = Counter([int(f) for f in list(fileinput.input())[0].split(",")])

    for i in range(DAYS):
        state = Counter(
            dict([(i[0] - 1, i[1]) for i in state.items()])
        )  # Decrement counters
        state[8] += state[-1]  # Spawn new fish
        state[6] += state[-1]  # Reset existing fish
        del state[-1]  # Clean up

    print(state.total())  # This requires Python 3.10+


if __name__ == "__main__":
    main()
