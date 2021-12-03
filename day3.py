def a():
    with open('input.txt') as f:
        lines = [line.rstrip() for line in f]

    most = ""
    least = ""
    for i in range(len(lines[0])):
        zero = 0
        one = 0
        for j in lines:
            if j[i] == "0":
                zero += 1
            else:
                one += 1
        if zero > one:
            most += "0"
            least += "1"
        else:
            most += "1"
            least += "0"

    most = int(most, 2)
    least = int(least, 2)
    print(most * least)


def b():
    with open('input.txt') as f:
        lines = [line.rstrip() for line in f]

    o = lines
    c = lines
    for i in range(0, len(lines[0])):
        o = parse(o, i, "most")
        if len(o) == 1:
            break
    for i in range(0, len(lines[0])):
        c = parse(c, i, "least")
        if len(c) == 1:
            break

    o = int(o[0], 2)
    c = int(c[0], 2)
    print(o * c)


def parse(array, index, order):
    zero = 0
    z = []
    one = 0
    o = []
    for i in range(len(array)):
        s = array[i]
        if s[index] == "0":
            zero += 1
            z.append(s)
        elif s[index] == "1":
            one += 1
            o.append(s)
    if zero > one:
        if order == "most":
            return z
        else:
            return o
    elif zero <= one:
        if order == "most":
            return o
        else:
            return z


if __name__ == '__main__':
    a()
    b()
