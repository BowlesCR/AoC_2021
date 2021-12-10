from collections import deque
import fileinput


def main() -> None:

    score = 0
    line: str
    for line in fileinput.input():
        score += checkline(line.strip())

    print(score)


def checkline(line: str) -> int:
    stack = deque()
    for c in line.strip():
        if c in ["(", "[", "{", "<"]:
            stack.append(c)
        else:
            oc = stack.pop()
            if c == ")" and oc != "(":
                return 3
            elif c == "]" and oc != "[":
                return 57
            elif c == "}" and oc != "{":
                return 1197
            elif c == ">" and oc != "<":
                return 25137
    return 0


if __name__ == "__main__":
    main()
