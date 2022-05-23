import random

def mutation(x):
    print("mutation")

def crossover(x1,x2):
    print("crossover")

def repeat(s, ch):
    for i in range(len(s)):
        if s[i] == ch:
            return True

    return False

population = k = 10

cities = 5

start = 0

#cities
genes =    "A  B  C  D  E"
original = [0, 1, 2, 3, 4]
orgchr =   [1, 2, 3, 4]
chromosomes = []

#creation of 10 random chromosomes
i = 0
while i < k:
    i = i + 1
    chr = random.sample(orgchr, len(orgchr))
    chr.insert(0, start)
    chr.append(start)
    chromosomes.append(chr)

print(chromosomes)

x = [0, 1, 2, 3, 4, 0]

#Cost
def cost(x):
    costos = 0
    for i in range(len(x) - 1):
        if x[i] == 0:  # A
            if x[i + 1] == 1:
                costos = costos + 4
            elif x[i + 1] == 2:
                costos = costos + 4
            elif x[i + 1] == 3:
                costos = costos + 7
            elif x[i + 1] == 4:
                costos = costos + 3
        elif x[i] == 1:  # B
            if x[i + 1] == 0:
                costos = costos + 4
            elif x[i + 1] == 2:
                costos = costos + 2
            elif x[i + 1] == 3:
                costos = costos + 3
            elif x[i + 1] == 4:
                costos = costos + 5
        elif x[i] == 2:  # C
            if x[i + 1] == 1:
                costos = costos + 2
            elif x[i + 1] == 0:
                costos = costos + 4
            elif x[i + 1] == 3:
                costos = costos + 2
            elif x[i + 1] == 4:
                costos = costos + 3
        elif x[i] == 3:  # D
            if x[i + 1] == 1:
                costos = costos + 3
            elif x[i + 1] == 2:
                costos = costos + 2
            elif x[i + 1] == 0:
                costos = costos + 7
            elif x[i + 1] == 4:
                costos = costos + 6
        elif x[i] == 4:  # E
            if x[i + 1] == 1:
                costos = costos + 5
            elif x[i + 1] == 2:
                costos = costos + 3
            elif x[i + 1] == 3:
                costos = costos + 6
            elif x[i + 1] == 0:
                costos = costos + 3
    costos = 1/costos
    return costos

#Athroisma kostous prwtwn tyxaiwn diadromwn
s = 0
for i in range(len(chromosomes)):
    cost(chromosomes[i])
    s = s + cost(chromosomes[i])

print(cost(chromosomes[0]))
print(s)

parents = []

def fitness(x):
    test = random.uniform(start, s)
    if cost(x) >= test:
        parents.append(x)
        print("good parent")


fitness(chromosomes[0])
#Vriskoyme ta xrwmoswmata poy einai kala parents
for i in range(len(chromosomes)):
    fitness(chromosomes[i])

print(parents)