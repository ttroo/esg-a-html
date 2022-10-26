def base_10(fn):
    def wrap(x, y):
        return fn(x + y) + 10
    return wrap

# ---

@base_10
def mysum2(x, y):
    return x + y

print(mysum2(1, 2))

# ---

# @base_10
# @base_10
# def mysum2(x, y):
#     return x + y

# print(mysum2(1, 2))

# ---

# mysum2 = base_10(mysum2)

# fn = mysum2 # 넘모 신기하당 !
# print(fn(1, 2))
# print(mysum2(1, 2))