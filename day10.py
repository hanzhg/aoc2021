def a():
    with open('input.txt') as f:
        lines = [list(line.rstrip()) for line in f]

    left = ["(", "{", "[", "<"]
    right = [")", "}", "]", ">"]
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    count = 0
    for i in lines:
        stack = []
        for j in i:
            if j in left:
                stack.append(j)
            else:
                s = right[left.index(stack.pop())]
                if j != s:
                    count += points[j]
                    break
    print(count)


if __name__ == '__main__':
    a()
