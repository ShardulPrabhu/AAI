import random
import math
print("Shardul Prabhu, 27")
def generate_population(Size, boundaries1, boundaries2):
    lowerboundary1, upperboundary1= boundaries1
    lowerboundary2, upperboundary2 = boundaries2
    Population = []
    for i in range(Size):
        Individual = {
            "x": random.uniform(lowerboundary1, upperboundary1),
            "y": random.uniform( lowerboundary2, upperboundary2),
        }
        Population.append(Individual)
    return Population

def apply_function(Individual):
    A = Individual["x"]
    B = Individual["y"]
    return math.sin(math.sqrt(A ** 2 + B ** 2))
gen = 10
Population = generate_population(Size=10, boundaries1=(-4, 4), boundaries2=(-4, 4))
i = 1
while True:
    print(f" GENERATION {i}")
    for Individual in Population:
        print(Individual)
    if i == gen:
        break
    i += 1

# Make next generation...
def choice_by_roulette(Sorted_pop, fitness_total):
    Offset = 0
    total_norm_fitness = fitness_total
    lowest_fitness1 = apply_function(Sorted_pop[0])
    if lowest_fitness1 < 0:
        Offset = -lowest_fitness1
        total_norm_fitness += Offset * len(Sorted_pop)
    Draw = random.uniform(0, 1)
    Accumulated = 0
    for Individual in Sorted_pop:
        Fit = apply_function(Individual) + Offset
        prob = Fit / total_norm_fitness
        Accumulated += prob
        if Draw <= Accumulated:
            return Individual

def sort_population_by_fitness(Population):
    return sorted(Population, key=apply_function)

def crossover(Individual_A, Individual_B):
    XA = Individual_A["x"]
    YA = Individual_A["y"]
    XB = Individual_B["x"]
    YB = Individual_B["y"]
    return {"x": (XA + XB) / 2, "y": (YA  + YB) / 2}

def mutate(Individual):
    xnext = Individual["x"] + random.uniform(-0.05, 0.05)
    ynext = Individual["y"] + random.uniform(-0.05, 0.05)
    Lboundary, Uboundary = (-4, 4)

# Guarantee we keep inside boundaries
    xnext = min(max(xnext, Lboundary), Uboundary)
    ynext = min(max(ynext, Lboundary), Uboundary)
    return {"x": xnext, "y": ynext}

def make_next_generation(prev_pop):
    next_gen = []
    sort_pop_fit = sort_population_by_fitness(prev_pop)
    pop_size = len(prev_pop)
    fitness_total = sum(apply_function(Individual) for Individual in Population)
    for i in range(pop_size):
        Choice1 = choice_by_roulette(sort_pop_fit, fitness_total)
        Choice2 = choice_by_roulette(sort_pop_fit, fitness_total)
        Individual = crossover(Choice1, Choice2)
        Individual = mutate(Individual)
        next_gen.append(Individual)
    return next_gen
gen = 10
Population = generate_population(Size=10, boundaries1=(-4, 4), boundaries2=(-4, 4))
i = 1
while True:
    print(f" GENERATION {i}")
    for Individual in Population:
        print(Individual, apply_function(Individual))
    if i == gen:
        break
    i += 1
    Population = make_next_generation(Population)
best_Individual = sort_population_by_fitness(Population)[-1]
print("\n FINAL RESULT")
print(best_Individual, apply_function(best_Individual))
