
# generate random integer values
from random import random
from random import seed
from random import randint
######################################################
# # seed random number generator
# seed(1)
# # generate some integers
# for i in range(5):
#     value = randint(0, 10)
#     # if value == 0:
#     #     print(">>",i,value)
#     #     break
#     print(">>", i, randint(-1, 3))
# print()

# for i in range(5):
#     value = randint(0, 10)
#     # if value == 0:
#     #     print(">>",i,value)
#     #     break
#     print(">>", i, int(random()*100*randint(0, 100)) % 4)
######################################################



def randomGene(length):
    randomGene = ""
    genes = ["C", "G", "T", "A"]
    for _ in range(length):
        randomGene += genes[randint(-1, 3)]
    return randomGene


def randomGenes():
    randomGenes = []
    for i in range(50):
        randomGenes.append(randomGene(randint(4, 500)))
        print(randomGenes[i])
        print("######################################")

    return randomGene

# print(randomGenes())


def randomGeneCombinationGenerator(over):
    randomGeneCombinations = []

    return randomGeneCombinations


def fact(n):
    return 1 if n == 0 else n*fact(n-1)


def removeDuplicate(itemsList):
    return list(set(itemsList))
