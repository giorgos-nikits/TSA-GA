import random


#Function for no repeat
def repeat(s, ch):
    for i in range(len(s)):
        for j in range(len(ch)):
            if s[i] == ch[j]:

                return True
            else:
                return False

def checkDupl(x):
    if len(x) == len(set(x)):
        return False
    else:
        return True



#creation of 10 random chromosomes
def genchr(k):
    i = 0
    while i < k:
        i = i + 1
        chr1 = random.sample(orgchr, len(orgchr))
        chr1.insert(0, start)
        chr1.append(start)
        chromosomes.append(chr1)
        
#Cost
def fitness(x):
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
    allfit.append(costos)
    return costos


#Athroisma kostous olwn twn xromosomatwn
def fitsum(x):
    s = 0
    for i in range(len(x)):
        s = s + x[i]
    return s

#epilogh gonewn
def selection(x):
    print("selection")
    val = 0
    count = 0
    #while count < 10:
    while len(parents) < k:
        for i in range(0, len(x)-1):
            test = random.uniform(start, fitsum(x))
            if test < (x[i]+val):
                if not(repeat(chromosomes[i], parents)):
                    parents.append(chromosomes[i])
                    print("hey")
                    val = val + allfit[i]
                    #count = count + 1
                    if len(parents) == k:
                        break
                else:
                    val = val + allfit[i]

#crossover
def crossover(x1, x2):
    print("crossover")
    count = 0
    offspring1 = []
    rest = []
    offspring2 = []
    for i in range(len(x1)):
        if i < 3:
            offspring1.append(x1[i])
            offspring2.append(x2[i])
        elif 3 <= i < 6:
            offspring1.append(x2[i])
            offspring2.append(x1[i])
    newchrom.append(offspring1)
    newchrom.append(offspring2)

def mutate(x):
    for i in range(len(x)):
        count1 = count2 = count3 = count4 = 0
        flag1 = flag2 = flag3 = flag4 = True
        for j in range(len(x[i]) - 1):
            if x[i][j] == 1:
                count1 = count1 + 1
                if count1 > 1 and flag1:
                    keepi = i
                    keepj = j
                    flag1 = False
            elif x[i][j] == 2:
                count2 = count2 + 1
                if count2 > 1 and flag2:
                    keepi = i
                    keepj = j
                    flag2 = False
            elif x[i][j] == 3:
                count3 = count3 + 1
                if count3 > 1 and flag3:
                    keepi = i
                    keepj = j
                    flag3 = False
            elif x[i][j] == 4:
                count4 = count4 + 1
                if count4 > 1 and flag4:
                    keepi = i
                    keepj = j
                    flag4 = False

            if count1 > 1:
                print(i, j)
                print("mutation of 1")
                if count2 == 0 and flag2:
                    x[i][j] = 2
                    count1 = 0
                    count2 = count2 + 1
                    flag2 = False
                elif count3 == 0 and flag3:
                    x[i][j] = 3
                    count1 = 0
                    count3 = count3 + 1
                    flag3 = False
                elif count4 == 0 and flag4:
                    x[i][j] = 4
                    count1 = 0
                    count4 = count4 + 1
                    flag4 = False
            elif count2 > 1:
                print(i, j)
                print("mutation of 2")
                if count1 == 0 and flag1:
                    x[i][j] = 1
                    count2 = 0
                    count1 = count1 + 1
                    flag1 = False
                elif count3 == 0 and flag3:
                    x[i][j] = 3
                    count2 = 0
                    count3 = count3 + 1
                    flag3 = False
                elif count4 == 0 and flag4:
                    x[i][j] = 4
                    count2 = 0
                    count4 = count4 + 1
                    flag4 = False
            elif count3 > 1:
                print(i, j)
                print("mutation of 3")
                if count2 == 0 and flag2:
                    x[i][j] = 2
                    count3 = 0
                    count2 = count2 + 1
                    flag2 = False
                elif count1 == 0 and flag1:
                    x[i][j] = 1
                    count3 = 0
                    count1 = count1 + 1
                    flag1 = False
                elif count4 == 0 and flag4:
                    x[i][j] = 4
                    count3 = 0
                    count4 = count4 + 1
                    flag4 = False
            elif count4 > 1:
                print(i, j)
                print("mutation of 4")
                if count2 == 0 and flag2:
                    x[i][j] = 2
                    count4 = 0
                    count2 = count2 + 1
                    flag2 = False
                elif count3 == 0 and flag3:
                    x[i][j] = 3
                    count4 = 0
                    count3 = count3 + 1
                    flag3 = False
                elif count1 == 0 and flag1:
                    x[i][j] = 1
                    count4 = 0
                    count1 = count1 + 1
                    flag1 = False




#Start

population = k = 10

cities = V = 5

start = 0

#cities

genes =    "A  B  C  D  E"
original = [0, 1, 2, 3, 4]
orgchr =   [1, 2, 3, 4]
chromosomes = []

allfit = []
parents = []

#start

#creation of 10 randmom solutions
print("Dhmioyrgia 10 random lysewn")
genchr(k)
print(chromosomes)

#next start

#Υπολογισμος fitness καθε διαδρομης
for i in range(len(chromosomes)):
    fitness(chromosomes[i])

#το fitness καθε διαδρομης αντιστοιχα
print("fitness kathe diadromis antistoixa")
print(allfit)

#αθροισμα fitness ολων των διαδρομων
print("Synolo fitness olwn twn diadromwn")
print(fitsum(allfit))


#epilegoyme toys goneis (kathe diadoxiko zeygari einai ena zeygari gonewn)
print("epilegoyme toys goneis (kathe diadoxiko zeygari einai ena zeygari gonewn)")
selection(allfit)
print(parents)

print("new children created by parents")
#crossover gia kathe zeygari gonewn
newchrom = []
for i in range(0, len(parents)-1, 2):
    crossover(parents[i], parents[i+1])

print("the new children after crossover")
print(newchrom)


#Mutation of new children
mutate(newchrom)
print(newchrom)








