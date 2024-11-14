from .individual import Individual
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .algorithm import DNA

class Population:
    def __init__(self, dna:'DNA', population_size:int, genome_size:int):
        self.individuals = [Individual(dna, genome_size) for _ in range(population_size)]

    def evaluate_population(self)->None:
        for individual in self.individuals:
            individual.calculate_fitness()

    def get_best_individual(self)->Individual:
        return max(self.individuals, key=lambda ind: ind.fitness)
