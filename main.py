# I found a math problem and thought it would be
# possible to solve it through a computer simulation.
# So i developed this simulation to solve it.
# The problem is:

# Encontrei um problema matemático e achei que seria
# possível resolvê-lo através de uma simulação computacional.
# Então desenvolvi esta simulação para resolvê-lo.
# O problema é o seguinte:

# Suppose that when rolling 30 6-sided dice, the result was 100.
# And suppose that one of the faces appeared 6 times.
# So how many times did each face come out?

# Suponha que, ao rolar 30 dados de 6 faces, obteve-se o resultado 100.
# E suponha que uma das faces saiu 6 vezes.
# Então, quantas vezes cada face saiu?

from random import randint

list_30_dices = []
list_quantity_each_face = []

for n in range(10000):
    for n2 in range(30):
        random_dice = randint(1, 6)
        list_30_dices.append(random_dice)
    sum_30_dices = sum(list_30_dices)
    if sum_30_dices == 100:
        num1 = list_30_dices.count(1)
        num2 = list_30_dices.count(2)
        num3 = list_30_dices.count(3)
        num4 = list_30_dices.count(4)
        num5 = list_30_dices.count(5)
        num6 = list_30_dices.count(6)
        list_quantity_each_face = [num1, num2, num3, num4, num5, num6]
        for n3 in list_quantity_each_face:
            if n3 > 6:
                list_quantity_each_face = []
        if list_quantity_each_face.count(6) == 1:
            print(f"""
Face 1: {num1}, 
face 2: {num2}, 
face 3: {num3}, 
face 4: {num4}, 
face 5: {num5}, 
face 6: {num6}.""")
    list_30_dices = []
    list_quantity_each_face = []




