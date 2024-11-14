from .strategy.selection_strategy import SelectionStrategy
from .strategy.mutation_strategy import MutationStrategy
from .strategy.crossover_strategy import CrossoverStrategy
from .strategy.fitness_strategy import FitnessStrategy
from .strategy.dna_strategy import DNAStrategy
from .population import Population
from .individual import Individual

class DNA:
    def __init__(self, dna_strategy: DNAStrategy):
        self.dna_strategy = dna_strategy

    def generate_genome(self, genome_size: int) -> list:
        return self.dna_strategy.generate_genome(genome_size)

    def get_random_genes(self, genes_size: int = 1) -> list:
        return self.dna_strategy.get_random_genes(genes_size)

    def get_genes(self):
        return self.dna_strategy.genes

    def get_target(self):
        return self.dna_strategy.target

    def get_selection(self):
        return self.dna_strategy.selection

    def get_crossover(self):
        return self.dna_strategy.crossover

    def get_mutation(self):
        return self.dna_strategy.mutation

    def get_fitness_function(self):
        return self.dna_strategy.fitness_function

class FitnessFunction:
    def __init__(self, fitness_strategy: FitnessStrategy):
        self.fitness_strategy = fitness_strategy

    def evaluate(self, genome):
        return self.fitness_strategy.evaluate(genome)

class Selection:
    def __init__(self, selection_strategy: SelectionStrategy):
        self.selection_strategy = selection_strategy

    def select_parents(self, population:Population)->tuple[Individual,Individual]:
        return self.selection_strategy.select_parents(population)

class Crossover:
    def __init__(self, crossover_strategy: CrossoverStrategy):
        self.crossover_strategy = crossover_strategy

    def crossover(self, parent1:Individual, parent2:Individual)->tuple[Individual, Individual]:
        return self.crossover_strategy.crossover(parent1, parent2)

class Mutation:
    def __init__(self, mutation_strategy: MutationStrategy):
        self.mutation_strategy = mutation_strategy

    def mutate(self, individual:Individual):
        return self.mutation_strategy.mutate(individual)

    def set_mutation_rate(self,mutation_rate:float):
        self.mutation_strategy.mutation_rate = mutation_rate

class GeneticAlgorithm:
    def __init__(self, dna:DNA, population_size:int, genome_size:int, generations:int, mutation_rate:float, bestFitness = None):
        # Initialize components and parameters
        self.dna = dna
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.dna.get_mutation().set_mutation_rate(mutation_rate)
        self.currentGen = 0
        self.bestFitness = bestFitness
        self.allBest = None
        self.population = Population(dna,population_size, genome_size)

    def run(self):
        # Evaluate initial population
        self.population.evaluate_population()
        for i in range(self.generations):
            best_individual = self.runSingleGenration()
        return best_individual
    
    def runSingleGenration(self):
        # Select and generate new offspring
        new_population = []
        # Evaluate the new population
        if(self.currentGen == 0):
            self.population.evaluate_population()
        while len(new_population) < len(self.population.individuals):
            # Select parents
            parent1, parent2 = self.dna.get_selection().select_parents(self.population)

            # Apply crossover
            offspring1, offspring2 = self.dna.get_crossover().crossover(parent1, parent2)

            # Apply mutation
            self.dna.get_mutation().mutate(offspring1)
            self.dna.get_mutation().mutate(offspring2)

            # Add offspring to new population
            new_population.extend([offspring1, offspring2])

        # Replace old population with new generation
        self.population.individuals = new_population[:len(self.population.individuals)]
        
        # Evaluate the new population
        self.population.evaluate_population()

        # Track best individual
        best_individual = self.population.get_best_individual()
        if self.allBest == None:
            self.allBest = best_individual
        elif best_individual.fitness > self.allBest.fitness:
            self.allBest = best_individual
        self.currentGen += 1
        print(f"Generation {self.currentGen}, Best Fitness: {best_individual.fitness}")
        return best_individual