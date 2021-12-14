import collections
import fileinput

# Counter method inspired by
# https://www.reddit.com/r/adventofcode/comments/rfzq6f/comment/hohbf0y/
# https://pastebin.com/U78GmZQQ


def main() -> None:
    lines = [line.strip() for line in fileinput.input()]

    chain = lines[0]

    pairs = collections.Counter()
    for i in range(len(lines[0]) - 1):
        pairs[chain[i : i + 2]] += 1

    rules: dict[str, str] = {}
    for line in lines[2:]:
        line = line.split(" -> ")
        rules[line[0]] = line[1]

    del lines, line

    for s in range(40):
        newpairs = collections.Counter()

        for pair_tuple in pairs.items():
            r = rules[pair_tuple[0]]
            newpairs[pair_tuple[0][0] + r] += pair_tuple[1]
            newpairs[r + pair_tuple[0][1]] += pair_tuple[1]

        pairs = newpairs

    elements = collections.Counter()
    for pair_tuple in pairs.items():
        elements[pair_tuple[0][0]] += pair_tuple[1]
        elements[pair_tuple[0][1]] += pair_tuple[1]

    elements[chain[0]] += 1
    elements[chain[-1]] += 1

    c = elements.most_common()

    print((c[0][1] - c[-1][1]) // 2)


if __name__ == "__main__":
    main()
