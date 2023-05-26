# Задача 10: На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

from random import randint

num_Money = int(input('Enter money: '))
quantity_Money = 0
money_1 = 0
money_2 = 0

for i in range(num_Money):
    quantity_Money = randint(0, 1)
    print(quantity_Money)

    if quantity_Money == 0:
        money_1 += 1
    else:
        money_2 += 1
if money_1 > money_2:
    print(f'{money_2} монет с гербом нужно перевернуть')    
elif money_1 == money_2:
    print(f'Количество монет с орлом и решкой одинаковое.')    
else:
    print(f'{money_1} монет с решкой нужно перевернуть')
    

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.


X = int(input('Enter number X: '))
Y = int(input('Enter number Y: '))
# S = X + Y
# P = X * Y
for i in range(X):
    for j in range(Y):
        if (X == i + j) and (Y == i * j):
            print(i, j)


# Задача 14: 
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.


N = abs(int(input('Enter number: ')))
num = 0
X = 2
for i in range(N):
    if num != 1:
        X = X ** i
        if X <= N:
            print(X)
            X = 2
        else:
            num = 1
    else:
        i = N