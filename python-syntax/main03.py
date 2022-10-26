
def mysum2(x, y):
    return x + y

def mysum3(x, y, z):
    return x + y + z

def mysum(*args): # 가변인자
    print("args :", args)

mysum(1,2) # 튜플 형태로 출력
mysum(1, 2, 3, 4, 5) # 튜플 형태로 출력

def mysum(*args): # 가변인자
    # result = 0
    # for number in args:
    #     result += number
    return sum(args)

print(mysum(1,2))
print(mysum(1, 2, 3, 4, 5))