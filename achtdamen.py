import random
import matplotlib.pyplot as plt

n = 8                          #Damen
p = 500                        #Populationen

aktuell_generation = []        #Aktuell Generation
neue_generation = []           #Neue Generation

def randomGeneration(Zeile,DamenNumber):
    generation_list = []
    for i in range(Zeile):
        gene = []
        for j in range(DamenNumber):
            gene.append(random.randint(1,n))
        gene.append(0)
        generation_list.append(gene)
    return generation_list

def fitness(population_list):
    i = 0
    konflikt = 0
    while i < len(population_list):
        j = 0
        konflikt = 0
        while j < n:
            l = j+1

            while l < n:
                if population_list[i][j] == population_list[i][l]:
                    konflikt+=1
                if abs(j-l)==abs(population_list[i][j]-population_list[i][l]):
                    konflikt+=1
                l+=1
            j+=1
        population_list[i][len(population_list[j])-1]=konflikt
        i+=1
        
    for i in range(len(population_list)):
        min = i
        for j in range(i,len(population_list)):
            if population_list[j][n]<population_list[min][n]:
                min = j
        temp =  population_list[i]
        population_list[i] = population_list[min]
        population_list[min] = temp
    return population_list
def cross_over(generation_list):
    for i in range(0,len(generation_list),2):
        z = 0
        neue_kid1 = []
        neue_kid2 = []
        while z<n:
            if(z<n//2):
                neue_kid1.append(generation_list[i][z])
                neue_kid2.append(generation_list[i+1][z])
            else:
                neue_kid1.append(generation_list[i+1][z])
                neue_kid2.append(generation_list[i][z])
            z+=1
        neue_kid1.append(0)
        neue_kid2.append(0)
        generation_list.append(neue_kid1)
        generation_list.append(neue_kid2)
    return generation_list
def mutation(generation_list):
    muted_list=[]
    i = 0
    while i<p//2:
        new_rand = random.randint(p//2,p-1)
        if new_rand not in muted_list:
            muted_list.append(new_rand)
            generation_list[new_rand][random.randint(0,n-1)]=random.randint(1,n-1)
            #print("Muted:",new_rand)
            i+=1
    return generation_list


def showRes(res):
    l = len(res)
    plt.figure(figsize=(6, 6))
    plt.scatter([x+1 for x in range(l - 1)], res[:l - 1])
    for i in range(l):
        plt.plot([0.5, l - 0.5], [i + 0.5, i + 0.5], color = "k")
        plt.plot([i + 0.5, i + 0.5], [0.5, l - 0.5], color = "k")
aktuell_generation = randomGeneration(p,n)
aktuell_generation = fitness(aktuell_generation)
epoch = 1
while True:
    
    aktuell_generation = aktuell_generation[0:p//2]
    neue_generation = cross_over(aktuell_generation)
    neue_generation = mutation(neue_generation)
    aktuell_generation = neue_generation
    aktuell_generation = fitness(aktuell_generation)
    if aktuell_generation[0][n] == 0:
        print("Solution",aktuell_generation[0])
        showRes(aktuell_generation[0])
        break
    else:
        print("Best Solution: ", aktuell_generation[0])
    