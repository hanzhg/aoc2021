import math


def parse():
    with open('input.txt') as f:
        lines = [line.strip().replace("  ", " ") for line in f]
    commands = lines[0].split(",")
    lines = [x for x in lines if x][1:]
    possibilities = []
    chunks = []

    for i in range(0, len(lines), 5):
        chunks.append(lines[i:i + 5])

    for i in chunks:
        a = []
        for j in range(5):
            a.append(i[j].split(" "))
            possibilities.append(i[j].split(" "))

        b = list(map(list, zip(*a)))
        for j in b:
            possibilities.append(j)

    valid_lines = []
    for i in possibilities:
        if all(item in commands for item in i):
            valid_lines.append(i)

    return commands, possibilities, valid_lines


def a():
    commands, possibilities, valid_lines = parse()

    for i in range(5, len(commands)):
        c = commands[:i]
        for j in valid_lines:
            if all(i in c for i in j):
                index = math.floor(possibilities.index(j) / 10) * 10

                board = []
                for k in range(index, index + 5):
                    board.append(possibilities[k])

                s = sum(map(sum, [list(map(int, i)) for i in board])) - sum(list(map(int, j)))
                for k in c:
                    if any(k in sublist for sublist in board) and (k not in j):
                        s -= int(k)
                return s * int(c[-1])


def b():
    commands, possibilities, valid_lines = parse()

    winners = []
    for i in range(5, len(commands)):
        c = commands[:i]
        for j in valid_lines:
            if all(i in c for i in j):
                index = math.floor(possibilities.index(j) / 10) * 10

                if index not in winners:
                    winners.append(index)

                if len(winners) == len(possibilities) // 10:
                    board = []
                    for k in range(index, index + 5):
                        board.append(possibilities[k])

                    s = sum(map(sum, [list(map(int, i)) for i in board])) - sum(list(map(int, j)))
                    for k in c:
                        if any(k in sublist for sublist in board) and (k not in j):
                            s -= int(k)
                    return s * int(c[-1])


if __name__ == '__main__':
    print(a())
    print(b())
