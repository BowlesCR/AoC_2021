import fileinput
from math import floor, ceil


def main() -> None:
    line: str
    lines = [line.strip() for line in fileinput.input()]

    last = lines.pop(0)
    while lines:
        line = f"[{last},{lines.pop(0)}]"

        tokens: list[str] = list(line)
        del line
        reduced = False
        while not reduced:
            reduced = True

            # Check for explodes
            depth = 0
            for i, token in enumerate(tokens):
                if token == "[":
                    depth += 1
                elif token == "]":
                    if depth > 4:
                        reduced = False

                        j = next(
                            (j for j in range(i - 5, -1, -1) if tokens[j].isdigit()),
                            None,
                        )
                        if j:
                            tokens[j] = str(int(tokens[j]) + int(tokens[i - 3]))

                        j = next(
                            (
                                j
                                for j in range(i + 1, len(tokens))
                                if tokens[j].isdigit()
                            ),
                            None,
                        )
                        if j:
                            tokens[j] = str(int(tokens[j]) + int(tokens[i - 1]))

                        tokens = tokens[: i - 4] + ["0"] + tokens[i + 1 :]

                        del j
                        break
                    depth -= 1
            del depth

            if not reduced:
                continue

            # Check for splits
            for i, token in enumerate(tokens):
                if token.isdigit() and int(token) >= 10:
                    t = int(token)
                    tokens = (
                        tokens[:i]
                        + ["[", str(floor(t / 2)), ",", str(ceil(t / 2)), "]"]
                        + tokens[i + 1 :]
                    )
                    del t
                    reduced = False
                    break
            del i, token
            last = "".join(tokens)
        del reduced
    del lines

    print(last)

    # Calc magnitude
    tokens: list[str] = list(last)
    while len(tokens) > 1:
        for i, token in enumerate(tokens):
            if token == "]":
                tokens = (
                    tokens[: i - 4]
                    + [(3 * int(tokens[i - 3])) + (2 * int(tokens[i - 1]))]
                    + tokens[i + 1 :]
                )
                break  # Need to start over because list has been modified

    print(tokens[0])


if __name__ == "__main__":
    main()
