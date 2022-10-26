
def mysum(*args):
    return sum(args)

print(mysum()) # 0이 출력됨


def mysum(x, y, *args):
    return x + y + sum(args)

print(mysum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))