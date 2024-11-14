import random
from ..defaults.selection import RouletteWheelSelection
from ..defaults.crossover import HalfCrossover
from ..defaults.mutation import ElementMutation
from ..defaults.fitness_function import MaximizeOnesFitness
from .selection_strategy import SelectionStrategy
from .crossover_strategy import CrossoverStrategy
from .mutation_strategy import MutationStrategy
from .fitness_strategy import FitnessStrategy

class DNAStrategy:
    def __init__(self, genes: list, target: list = None,
                duplicate_genomes: bool = True,
                 selection_strategy: SelectionStrategy = RouletteWheelSelection(),
                 crossover_strategy: CrossoverStrategy = HalfCrossover(),
                 mutation_strategy: MutationStrategy = ElementMutation(),
                 fitness_strategy: FitnessStrategy = MaximizeOnesFitness()):
        from ..algorithm import Selection, Crossover, Mutation, FitnessFunction
        self.selection = Selection(selection_strategy)
        self.crossover = Crossover(crossover_strategy)
        self.mutation = Mutation(mutation_strategy)
        self.fitness_function = FitnessFunction(fitness_strategy)
        self.genes = genes
        self.target = target
        self.duplicate_genomes = duplicate_genomes

    def __init_subclass__(cls, **kwargs):
        # Check if the subclass has overridden __init__
        if '__init__' in cls.__dict__:
            raise TypeError(f"{cls.__name__} cannot override the __init__ method.")
        super().__init_subclass__(**kwargs)

    def generate_genome(self, genome_size: int) -> list:
        if self.duplicate_genomes:
            return random.choices(self.genes, k=genome_size)
        else:
            if genome_size > len(self.genes):
                raise ValueError("Error: Genome size must be less than or equal to the length of genes.")
            else:
                random.shuffle(self.genes)
                return self.genes[:genome_size]

    def get_random_genes(self, genes_size: int = 1) -> list:
        return random.choices(self.genes, k=genes_size)
