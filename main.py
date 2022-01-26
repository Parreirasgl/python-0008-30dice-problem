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

def generate_list_30_dices():
    for n in range(30):
        random_dice = randint(1, 6)
        list_30_dices.append(random_dice)
    return


def generate_list_quantity_each_face():
    list_quantity_each_face.append(list_30_dices.count(1))
    list_quantity_each_face.append(list_30_dices.count(2))
    list_quantity_each_face.append(list_30_dices.count(3))
    list_quantity_each_face.append(list_30_dices.count(4))
    list_quantity_each_face.append(list_30_dices.count(5))
    list_quantity_each_face.append(list_30_dices.count(6))
    return


from random import randint

NUMBER_SIMULATIONS = 10000
list_30_dices = []
list_quantity_each_face = []
list_correct_results = []
counter = 0

for n in range(NUMBER_SIMULATIONS):
    generate_list_30_dices()
    sum_30_dices = sum(list_30_dices)
    if sum_30_dices == 100:
        generate_list_quantity_each_face()
        if max(list_quantity_each_face) == 6 and list_quantity_each_face.count(6) == 1:
            counter += 1
            list_correct_results = list_quantity_each_face
        else:
            list_quantity_each_face = []
    list_30_dices = []
    list_quantity_each_face = []

print(f"""
Face 1 appeard {list_correct_results[0]} times. 
face 2 appeard {list_correct_results[1]} times. 
face 3 appeard {list_correct_results[2]} times. 
face 4 appeard {list_correct_results[3]} times. 
face 5 appeard {list_correct_results[4]} times. 
face 6 appeard {list_correct_results[5]} times.
""")
print(f"This pattern occurred {counter} times during the simulation.")