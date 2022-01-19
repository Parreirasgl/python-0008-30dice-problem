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

list = []
list2 = []

for n in range(10):
    for n in range(30):
        aleat = randint(1,6)
        list.append(aleat)
    sum1 = sum(list)
    print(sum1)

