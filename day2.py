def a():
    with open('input.txt') as f:
        lines = [line.rstrip().split(" ") for line in f]
    hp = 0
    depth = 0
    for i in lines:
        if i[0] == "forward":
            hp += int(i[1])
        if i[0] == "down":
            depth += int(i[1])
        if i[0] == "up":
            depth -= int(i[1])
    print(hp * depth)


def b():
    with open('input.txt') as f:
        lines = [line.rstrip().split(" ") for line in f]
    hp = 0
    depth = 0
    aim = 0

    for i in lines:
        if i[0] == "forward":
            hp += int(i[1])
            depth += aim * int(i[1])
        if i[0] == "down":
            aim += int(i[1])
        if i[0] == "up":
            aim -= int(i[1])
    print(hp * depth)


if __name__ == '__main__':
    a()
    b()
