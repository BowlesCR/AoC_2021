import fileinput


def main() -> None:
    acc = 0

    line: str
    for line in fileinput.input():
        line.strip()
        line = line.split("|")

        pats = line[0].split()
        nums = {
            1: frozenset(next(p for p in pats if len(p) == 2)),
            4: frozenset(next(p for p in pats if len(p) == 4)),
            7: frozenset(next(p for p in pats if len(p) == 3)),
            8: frozenset(next(p for p in pats if len(p) == 7)),
        }

        p5 = [p for p in pats if len(p) == 5]
        p6 = [p for p in pats if len(p) == 6]
        del pats

        nums[6] = frozenset(next(p for p in p6 if not set(p).issuperset(nums[1])))

        nums[3] = frozenset(next(p for p in p5 if set(p).issuperset(nums[1])))

        nums[5] = frozenset(next(p for p in p5 if set(p).issubset(nums[6])))

        nums[2] = frozenset(next(p for p in p5 if set(p) | nums[5] == nums[8]))

        nums[0] = frozenset(next(p for p in p6 if set(p) | nums[5] == nums[8]))

        nums[9] = frozenset(next(p for p in p6 if set(p) | nums[3] != nums[8]))

        del p5, p6

        nums = {v: k for k, v in nums.items()}
        assert len(nums) == 10, "Identifying nums went wrong"

        num = 0
        for o in line[1].split():
            num = num * 10 + nums[frozenset(o)]

        acc += num

    print(acc)


if __name__ == "__main__":
    main()
