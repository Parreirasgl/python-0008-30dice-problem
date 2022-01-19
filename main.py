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

list_a = []
list_b = []

for n in range(10000):
    for n2 in range(30):
        aleat = randint(1, 6)
        list_a.append(aleat)
    sum_dices = sum(list_a)
    if sum_dices == 100:
        num1 = list_a.count(1)
        num2 = list_a.count(2)
        num3 = list_a.count(3)
        num4 = list_a.count(4)
        num5 = list_a.count(5)
        num6 = list_a.count(6)
        list_b = [num1, num2, num3, num4, num5, num6]
        for n3 in list_b:
            if n3 > 6:
                list_b = []
        if list_b.count(6) == 1:
            print(f"""
Face 1: {num1}, 
face 2: {num2}, 
face 3: {num3}, 
face 4: {num4}, 
face 5: {num5}, 
face 6: {num6}.""")
    list_a = []
    list_b = []




