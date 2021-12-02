import fileinput
import sys


def main() -> None:

    b = c = 0

    last: int = sys.maxsize
    count = 0

    for s in fileinput.input():
        a = b
        b = c
        c = int(s)
        if a and b and c:
            curr = a + b + c
            if curr > last:
                count += 1
            last = curr

    print(count)


if __name__ == "__main__":
    main()
