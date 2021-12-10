import statistics
from collections import deque
import fileinput


def main() -> None:
    lines: list[str] = [line.strip() for line in fileinput.input()]
    scores: list[int] = []
    for line in lines:
        score = checkline(line)
        if score:
            scores.append(score)

    print(statistics.median(scores))


def checkline(line: str) -> int:
    stack = deque()
    for c in line.strip():
        if c in ["(", "[", "{", "<"]:
            stack.append(c)
        else:
            oc = stack.pop()
            if c == ")" and oc != "(":
                return 0
            elif c == "]" and oc != "[":
                return 0
            elif c == "}" and oc != "{":
                return 0
            elif c == ">" and oc != "<":
                return 0

    score = 0
    while stack:
        oc = stack.pop()
        if oc == "(":
            score = score * 5 + 1
        elif oc == "[":
            score = score * 5 + 2
        elif oc == "{":
            score = score * 5 + 3
        elif oc == "<":
            score = score * 5 + 4
    return score


if __name__ == "__main__":
    main()
