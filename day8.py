def a():
    with open('input.txt') as f:
        lines = [line.rstrip() for line in f]
    count = 0
    for i in lines:
        a, b = i.split(" | ")
        b = b.split(" ")
        for j in b:
            if len(j) in [2, 3, 4, 7]:
                count += 1
    print(count)


if __name__ == '__main__':
    a()
