def a():
    with open('input.txt') as f:
        lines = [line.rstrip() for line in f]
    count = 0

    for i in range(len(lines) - 1):
        a = int(lines[i])
        b = int(lines[i + 1])

        if b > a:
            count += 1
    print(count)


def b():
    with open('input.txt') as f:
        lines = [line.rstrip() for line in f]
    count = 0

    for i in range(len(lines) - 3):
        a = int(lines[i])
        b = int(lines[i + 1])
        c = int(lines[i + 2])
        d = int(lines[i + 3])

        current = a + b + c
        next = b + c + d
        if next > current:
            count += 1
    print(count)


if __name__ == '__main__':
    a()
    b()
