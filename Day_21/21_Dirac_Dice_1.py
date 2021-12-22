import fileinput


def main():
    lines = list(fileinput.input())
    pos1 = int(lines[0].split()[-1])
    pos2 = int(lines[1].split()[-1])

    score1 = 0
    score2 = 0

    die = Die()

    while score1 < 1000 and score2 < 1000:
        pos1 += die.roll() + die.roll() + die.roll()
        pos1 = (pos1 - 1) % 10 + 1
        score1 += pos1

        if score1 >= 1000:
            break

        pos2 += die.roll() + die.roll() + die.roll()
        pos2 = (pos2 - 1) % 10 + 1
        score2 += pos2

    print(min(score1, score2) * die.rolls)


class Die:
    def __init__(self):
        self.rolls = 0
        self.value = 99

    def roll(self) -> int:
        self.rolls += 1
        self.value = (self.value + 1) % 100
        return self.value + 1


if __name__ == "__main__":
    main()
