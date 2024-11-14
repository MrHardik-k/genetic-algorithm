from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .algorithm import DNA

class Individual:
    def __init__(self, dna:'DNA', genome_size:int):
        self.dna = dna
        self.genome = self.generate_genome(genome_size)
        self.fitness = None
        if self.dna.get_fitness_function() != None:
            self.fitness = self.calculate_fitness()

    def generate_genome(self, genome_size:int)->list:
        return self.dna.generate_genome(genome_size)

    def calculate_fitness(self):
        self.fitness = self.dna.get_fitness_function().evaluate(self.genome)
        return self.fitness
