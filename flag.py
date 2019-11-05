from sys import argv, exit


def flag(n):
    if type(n) != int or n <= 0 or n % 2 == 1:
        raise Exception('ArgumentError')

    vert_dist = int(n/2)
    circle = ""
    flag = "#" * (n*3+2) + "\n"

    for i in range(vert_dist):
        circle += "#{:^{width}}#\n".format("*{}*".format("o"*i*2), width=n*3)
        flag += "#{:^{width}}#\n".format(" ", width=n*3)

    flag += circle
    flag = flag[:-1] + flag[::-1]
    return flag


if __name__ == "__main__":
    try:
        n = int(argv[1])
    except ValueError:
        exit("N must be an integer.")

    print(flag(n))
