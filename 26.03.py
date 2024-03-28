№27
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
b = [18 ,19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42]
c = list(set(a+b))
print (c)
# Задача 28
b = [[1,0,2],[1,2,0],[0,1,5]]
count=int()
print (b)
for row in b:
    for num in row:
        if num == 0:
            count+=1
print(count)
# Задача 29
b = [[1,0,-2],[1,2,0],[0,-1,5]]
a = 1 
print (b)
for row in b:
    for num in row:
        if num < 0:
            a *= num
print (a)
