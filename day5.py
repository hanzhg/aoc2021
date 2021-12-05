def main():
    with open('input.txt') as f:
        lines = [line.strip() for line in f]
    grid = [[0 for j in range(1000)] for i in range(1000)]
    grid2 = [[0 for j in range(1000)] for i in range(1000)]
    count = 0
    count2 = 0
    for i in lines:
        x1, y1, x2, y2 = [int(n) for n in i.replace(",", " ").replace(" -> ", " ").split(" ")]
        if x1 == x2 or y1 == y2:
            for j in range(min(x1, x2), max(x1, x2) + 1):
                for k in range(min(y1, y2), max(y1, y2) + 1):
                    grid[j][k] += 1
                    grid2[j][k] += 1
        else:
            if x1 > x2:
                x1, x2 = x2, x1
                y1, y2 = y2, y1

            m = (y2 - y1) // abs(x2 - x1)
            for inc, x in enumerate(range(x1, x2 + 1)):
                y = m * inc + y1
                grid2[x][y] += 1

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] > 1:
                count += 1
            if grid2[i][j] > 1:
                count2 += 1

    print(count)
    print(count2)


if __name__ == '__main__':
    main()
