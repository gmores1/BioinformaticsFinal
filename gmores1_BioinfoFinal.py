#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 10 22:07:04 2022

@author: graycemores
"""

import random, sys, matplotlib.pyplot as plt
class orca:
    population = None
    birthRate = None
    deathRate = None
    
    def __init__(self, pop, birth, death):
        self.population = pop
        self.birthRate = birth
        self.deathRate = death
    def summarize(self):
        print("The orca population is %f, with a birth rate of %f and a death rate of %f." % (self.population, self.birthRate, self.deathRate))

### Set values for penguin population, birth rate, and death rate. ###
orcaPop = random.randint(1,20)
orcaBirth = random.random()
orcaDeath = random.random()
#sys.argv for birth rate and death rate
#use 0 to flag whether the user wants to use a random value or input value
orcaValue1 = orca(orcaPop, orcaBirth, orcaDeath)
orcaValue1.summarize()

class seal:
    population = None
    birthRate = None
    deathRate = None
    
    def __init__(self, pop, birth, death):
        self.population = pop
        self.birthRate = birth
        self.deathRate = death
    def summarize(self):
        print("The seal population is %f, with a birth rate of %f and a death rate of %f." % (self.population, self.birthRate, self.deathRate))

### Set values for seal population, birth rate, and death rate. ###
sealPop = random.randint(10,100)
sealBirth = random.random()
sealDeath = random.random()
sealValue1 = seal(sealPop, sealBirth, sealDeath)
sealValue1.summarize()

class penguin:
    population = None
    birthRate = None
    deathRate = None
    
    def __init__(self, pop, birth, death):
        self.population = pop
        self.birthRate = birth
        self.deathRate = death
    def summarize(self):
        print("The penguin population is %f, with a birth rate of %f and a death rate of %f." % (self.population, self.birthRate, self.deathRate))

### Set values for penguin population, birth rate, and death rate. ###
penguinPop = random.randint(40,200)
penguinBirth = random.random()
penguinDeath = random.random()
penguinValue1 = penguin(penguinPop, penguinBirth, penguinDeath)
penguinValue1.summarize()

### Create arrays to store population values from each time step. ###
t = []
orcaData = []
sealData = []
penguinData = []
orcaChange = 0
sealChange = 0
penguinChange = 0


### Define maximum carrying capacity of the study environment, along with desired times of measurement ###
time_step = 0.01
max_time = 90
carrying_capacity = 100*min(orcaValue1.deathRate, sealValue1.deathRate, penguinValue1.deathRate)

### Functions that change the population of each organism based on birth and death rates. ###
def orca_population(orcaPop, orcaBirth, orcaDeath, sealPop, penguinPop, carrying_capacity, time_step):
    """Updates the orca population"""
    gain = orcaBirth * orcaPop
    loss = orcaDeath * orcaPop * (orcaPop + sealPop + penguinPop)/float(carrying_capacity)
    orcaChange = (gain - loss) * time_step
    return round(orcaChange, 0)

def seal_population(sealPop, sealBirth, sealDeath, orcaPop, penguinPop, carrying_capacity, time_step):
    gain = sealBirth * sealPop #birth_rate*population
    loss = sealDeath * sealPop * (orcaPop + sealPop + penguinPop)/float(carrying_capacity)
    sealChange = (gain - loss) * time_step
    return round(sealChange, 0)

def penguin_population(penguinPop, penguinBirth, penguinDeath, orcaPop, sealPop, carrying_capacity, time_step):
    gain = penguinBirth * penguinPop #birth_rate*population
    loss = penguinDeath * penguinPop * (orcaPop + sealPop + penguinPop)/float(carrying_capacity)
    penguinChange = (gain - loss) * time_step
    return round(penguinChange, 0)

### Run the simulation and update population values ###
for i in range (1, max_time):
    time = i
    
    orcaPop += orca_population(orcaPop, orcaBirth, orcaDeath, sealPop, penguinPop, carrying_capacity, time_step)
    sealPop += seal_population(sealPop, sealBirth, sealDeath, orcaPop, penguinPop, carrying_capacity, time_step)
    penguinPop += penguin_population(penguinPop, penguinBirth, penguinDeath, orcaPop, sealPop, carrying_capacity, time_step)
    
    t.append(time)
    orcaData.append(orcaPop)
    sealData.append(sealPop)
    penguinData.append(penguinPop)
    
    i = i+1

### Graph the results of population change over time ###

def graph(t, sealData, orcaData, penguinData):
    #Orca Population
    plt.plot([t], [orcaData])
    plt.xlabel("Generations")
    plt.ylabel("Population")
    plt.title("Orca Population")
    plt.show()
    
    #Seal Population
    plt.plot([t], [sealData])
    plt.xlabel("Generations")
    plt.ylabel("Population")
    plt.title("Seal Population")
    plt.show()
    
    #Penguin Population
    plt.plot([t], [penguinData])
    plt.xlabel("Generations")
    plt.ylabel("Population")
    plt.title("Penguin Population")
    plt.show()
    
    #All 3 Populations
    x = [t]
    y1 = [orcaData]
    y2 = [sealData]
    y3 = [penguinData]
    plt.title("Average Populations in a Predator-Prey Food Chain")
    plt.xlabel("Generations")
    plt.ylabel("Population")
    plt.gca().legend(('y1','y2','y3'))
    plt.plot(x, y1, "-r", label ="Orcas")
    plt.plot(x, y2, "-b", label ="Seals")
    plt.plot(x, y3, "-g", label ="Penguins")

graph(time, sealData, orcaData, penguinData)