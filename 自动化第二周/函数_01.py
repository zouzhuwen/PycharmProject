def count(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum

list = [1,2,3,4,5,6,7]
num = count(*list)
print(num)