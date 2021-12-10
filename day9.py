def a():
    with open('input.txt') as f:
        lines = [line.rstrip() for line in f]

    array = []

    for i in range(len(lines)):
        array.append([int(j) for j in lines[i]])

    points = []
    for x in range(len(array)):
        for y in range(len(array[x])):
            target = array[x][y]
            if x < len(array) - 1:
                if array[x + 1][y] <= target:
                    continue
            if x > 0:
                if array[x - 1][y] <= target:
                    continue
            if y < len(array[x]) - 1:
                if array[x][y + 1] <= target:
                    continue
            if y > 0:
                if array[x][y - 1] <= target:
                    continue
            points.append((x, y))
    count = 0

    for i in points:
        count += array[i[0]][i[1]] + 1
    print(count)


if __name__ == '__main__':
    a()
