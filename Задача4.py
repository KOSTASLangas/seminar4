# Задайте два числа. Напишите программу, которая найдет НОК (наименьшее общее кратное) этих двух чисел. 

a, b = list(map(int, input().split()))
flag = True
for i in range(2, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        print(i)
        flag = False
if flag:
    print('нет общего делителя')
