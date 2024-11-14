from ..strategy.fitness_strategy import FitnessStrategy

class CompairTargetFitness(FitnessStrategy):
    def __init__(self, target:list):
        self.target = target

    def evaluate(self, genome:list)->float:
        fitness = 0
        for i in range(len(genome)):
            if self.target[i] == genome[i]:
                fitness += 1
        return fitness


class MaximizeOnesFitness(FitnessStrategy):
    def evaluate(self, genome):
        """Fitness is the number of 1's in the genome."""
        return sum(genome)

class MinimizeDistanceFitness(FitnessStrategy):
    def __init__(self, target_value):
        super().__init__()
        self.target_value = target_value
    
    def evaluate(self, genome):
        """Fitness is the negative distance to the target value."""
        # Assuming the genome represents a single real-valued number
        value = sum(g * (2**i) for i, g in enumerate(reversed(genome)))  # Binary-to-decimal conversion
        return -abs(self.target_value - value)  # Negative distance (lower is better)

class WeightedSumFitness(FitnessStrategy):
    def __init__(self, weights):
        super().__init__()
        self.weights = weights

    def evaluate(self, genome):
        """Fitness is the weighted sum of the genome bits."""
        return sum(g * w for g, w in zip(genome, self.weights))