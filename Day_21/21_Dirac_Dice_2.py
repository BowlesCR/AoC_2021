import fileinput
import itertools
from functools import cache

rolls = [sum(x) for x in itertools.product([1, 2, 3], repeat=3)]


def main():
    lines = list(fileinput.input())
    pos1 = int(lines[0].split()[-1])
    pos2 = int(lines[1].split()[-1])

    print(max(game(pos1, pos2, 0, 0, 1)))


@cache
def game(pos1: int, pos2: int, score1: int, score2: int, player: int):
    # Inspiration from https://github.com/yoshivda/aoc2021/blob/master/days/day21.py
    if score1 >= 21:
        return 1, 0
    elif score2 >= 21:
        return 0, 1

    if player == 1:
        new_positions = [(pos1 + roll - 1) % 10 + 1 for roll in rolls]
        games = (
            game(newpos, pos2, score1 + newpos, score2, 2) for newpos in new_positions
        )
    elif player == 2:
        new_positions = [(pos2 + roll - 1) % 10 + 1 for roll in rolls]
        games = (
            game(pos1, newpos, score1, score2 + newpos, 1) for newpos in new_positions
        )

    games = list(games)
    return sum(g[0] for g in games), sum(g[1] for g in games)


if __name__ == "__main__":
    main()
