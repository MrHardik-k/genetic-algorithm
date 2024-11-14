import random
import math
from ..strategy.selection_strategy import SelectionStrategy
from ..individual import Individual
from ..population import Population

# Roulette Wheel Selection
class RouletteWheelSelection(SelectionStrategy):
    def select_parents(self, population:Population)->tuple[Individual, Individual]:
        fitness_values = [individual.fitness for individual in population.individuals]
        total_fitness = sum(fitness_values)
        selection_probs = [fitness / total_fitness for fitness in fitness_values]
        return random.choices(population.individuals, weights=selection_probs, k=2)

# Tournament Selection
class TournamentSelection(SelectionStrategy):
    def __init__(self, tournament_size=3):
        self.tournament_size = tournament_size

    def select_parents(self, population):
        tournament = random.sample(population.individuals, self.tournament_size)
        return max(tournament, key=lambda ind: ind.fitness)

# Rank Selection
class RankSelection(SelectionStrategy):
    def select_parents(self, population):
        sorted_population = sorted(population.individuals, key=lambda ind: ind.fitness)
        rank_weights = [i for i in range(1, len(population.individuals) + 1)]
        selected = random.choices(sorted_population, weights=rank_weights, k=1)
        return selected[0]

# Stochastic Universal Sampling (SUS)
class StochasticUniversalSampling(SelectionStrategy):
    def __init__(self, num_select=2):
        self.num_select = num_select

    def select_parents(self, population):
        total_fitness = sum(ind.fitness for ind in population.individuals)
        point_distance = total_fitness / self.num_select
        start_point = random.uniform(0, point_distance)
        pointers = [start_point + i * point_distance for i in range(self.num_select)]
        selected = []
        for point in pointers:
            cumulative = 0
            for ind in population.individuals:
                cumulative += ind.fitness
                if cumulative >= point:
                    selected.append(ind)
                    break
        return selected

# Elitism Selection
class ElitismSelection(SelectionStrategy):
    def __init__(self, num_elites=1):
        self.num_elites = num_elites

    def select_parents(self, population):
        sorted_population = sorted(population.individuals, key=lambda ind: ind.fitness, reverse=True)
        return sorted_population[:self.num_elites]

# Truncation Selection
class TruncationSelection(SelectionStrategy):
    def __init__(self, percentage=0.5):
        self.percentage = percentage

    def select_parents(self, population):
        sorted_population = sorted(population.individuals, key=lambda ind: ind.fitness, reverse=True)
        num_to_select = int(len(population.individuals) * self.percentage)
        return sorted_population[:num_to_select]

# Boltzmann Selection
class BoltzmannSelection(SelectionStrategy):
    def __init__(self, temperature=1.0):
        self.temperature = temperature

    def select_parents(self, population):
        boltzmann_weights = [math.exp(ind.fitness / self.temperature) for ind in population.individuals]
        total = sum(boltzmann_weights)
        probabilities = [weight / total for weight in boltzmann_weights]
        selected = random.choices(population.individuals, weights=probabilities, k=1)
        return selected[0]

# Steady-State Selection
class SteadyStateSelection(SelectionStrategy):
    def __init__(self, num_replacements=2):
        self.num_replacements = num_replacements

    def select_parents(self, population):
        sorted_population = sorted(population.individuals, key=lambda ind: ind.fitness)
        return sorted_population[-self.num_replacements:]

# Rank-Biased Selection
class RankBiasedSelection(SelectionStrategy):
    def __init__(self, bias_factor=0.7):
        self.bias_factor = bias_factor

    def select_parents(self, population):
        sorted_population = sorted(population.individuals, key=lambda ind: ind.fitness)
        num_individuals = len(population.individuals)
        weights = [(self.bias_factor ** (num_individuals - i)) for i in range(num_individuals)]
        selected = random.choices(sorted_population, weights=weights, k=1)
        return selected[0]
  