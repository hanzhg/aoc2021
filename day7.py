import statistics


def a():
    with open('input.txt') as f:
        lines = [int(i) for i in f.read().split(",")]

    median = statistics.median(lines)
    count = 0
    for i in lines:
        count += abs(median - i)
    print(int(count))


def b():
    with open('input.txt') as f:
        lines = [int(i) for i in f.read().split(",")]

    max_v = max(lines)
    min_v = min(lines)
    array = []
    for t in range(min_v, max_v + 1):
        count = 0
        for i in lines:
            a = abs(t - i)
            count += (a * (a + 1)) // 2
        array.append(count)
    print(min(array))


if __name__ == '__main__':
    a()
    b()
