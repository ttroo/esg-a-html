def base(base_number):
    def wrap(x, y):
        return x + y + base_number
    return wrap

base_10 = base(10)
base_20 = base(20)
base_30 = base(30)

print(base_10(1, 2))
print(base_20(1, 2))
print(base_30(1, 2))