
def mysum(x,y=0): # 디폴트인자
    return 10 * x + y

print(mysum(1, 2)) # 위치인자
print(mysum(2, 1)) # 위치인자
print(mysum(y=2, x=1)) # 키워드인자, 신기하다~~~

print(mysum(1)) # 디폴트인자, 신기하다~~~

print(mysum(1, y=2)) # 가능
# print(mysum(y=2, 1)) # 불가능