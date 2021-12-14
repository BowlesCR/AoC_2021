import collections
import fileinput


def main() -> None:

    lines = [line.strip() for line in fileinput.input()]

    chain: str = lines[0]

    rules: dict[str, str] = {}
    for line in lines[2:]:
        line = line.split(" -> ")
        rules[line[0]] = line[1]

    del line, lines

    for s in range(10):
        newchain: str = ""
        for i, v in enumerate(chain):
            if i == 0:
                newchain += chain[i]
            else:
                newchain += rules[chain[i - 1] + v] + v

        chain = newchain

    c = collections.Counter(chain).most_common()

    print(c[0][1] - c[-1][1])


if __name__ == "__main__":
    main()
