import fileinput

boards: list[list[list[str]]] = []


def main() -> None:

    lines: list[str] = list(fileinput.input())

    draws = lines.pop(0).split(",")

    while lines:
        lines.pop(0)
        board = []
        for i in range(5):
            board.append(lines.pop(0).split())
        boards.append(board)

    for num in draws:
        callNum(num)
        board = checkBoards()
        if board:
            score = 0
            for r in board:
                score += sum([int(c) for c in r if c])
            score *= int(num)
            print(score)
            break


def callNum(num) -> None:
    for b in range(len(boards)):
        for r in range(5):
            for c in range(5):
                if boards[b][r][c] == num:
                    boards[b][r][c] = ""


def checkBoards():
    for board in boards:
        for row in board:
            if "".join(row) == "":
                if len(boards) == 1:
                    return board
                elif board in boards:
                    boards.remove(board)

        for c in range(5):
            col = [board[r][c] for r in range(5)]
            if "".join(col) == "":
                if len(boards) == 1:
                    return board
                elif board in boards:
                    boards.remove(board)

    return None


if __name__ == "__main__":
    main()
