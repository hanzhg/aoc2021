def a():
    with open('input.txt') as f:
        lines = [int(i) for i in f.read().split(",")]

    count = [lines.count(i) for i in range(9)]

    for i in range(256):
        t = count[0]
        for j in range(8):
            count[j] = count[j + 1]
        count[8] = t
        count[6] += t

    print(sum(count))


if __name__ == '__main__':
    a()
