
# Genetic Algorithm Library

`genetic_algorithm_py` is a Python library for implementing genetic algorithms with customizable components. 
This library is designed to allow easy customization and extension, making it suitable for various optimization problems.

## Features
- Customizable selection, crossover, mutation, and fitness strategies.
- Predefined strategies in the `defaults` module for common use cases.
- Modular design to facilitate integration with different types of genetic algorithms.

---

## Installation

```bash
pip install genetic_algorithm_py
```

---

## Getting Started

### Basic Example

Here is a simple example to get started:

```python
from genetic_algorithm_py import GeneticAlgorithm, Population, Individual
from genetic_algorithm_py.defaults import RouletteWheelSelection, OnePointCrossover, BitFlipMutation, MaximizeOnesFitness

# Define parameters
population_size = 100
genome_length = 50
mutation_rate = 0.01
num_generations = 100

# Create components
selection_strategy = RouletteWheelSelection()
crossover_strategy = OnePointCrossover()
mutation_strategy = BitFlipMutation(mutation_rate=mutation_rate)
fitness_function = MaximizeOnesFitness()

# Create population
population = Population(size=population_size, genome_length=genome_length, fitness_function=fitness_function)

# Initialize and run genetic algorithm
ga = GeneticAlgorithm(
    population=population,
    selection_strategy=selection_strategy,
    crossover_strategy=crossover_strategy,
    mutation_strategy=mutation_strategy
)
ga.run(num_generations=num_generations)

# Get best individual
best_individual = ga.get_best_individual()
print("Best solution:", best_individual.genome)
print("Fitness:", best_individual.fitness)
```

---

## Documentation

### 1. Defaults Module

The `defaults` module provides ready-to-use implementations for common strategies.

#### 1.1 Crossover Strategies

The following crossover strategies are available in `defaults/crossover.py`:

- **HalfCrossover**: Splits genomes in half and swaps segments.
- **OnePointCrossover**: Performs a one-point crossover by selecting a random point and swapping segments.
- **TwoPointCrossover**: Performs a two-point crossover by selecting two points and swapping segments between them.
- **UniformCrossover**: Randomly selects genes from each parent to create offspring.
- **BlendCrossover**: Generates offspring genes within an extended range around each gene pair (controlled by `alpha`).
- **ArithmeticCrossover**: Averages gene pairs based on a blending factor (`alpha`).
- **PMXCrossover**: Partially Matched Crossover, suitable for permutation-based problems.

#### 1.2 Fitness Strategies

Defined in `defaults/fitness_function.py`:

- **CompairTargetFitness**: Measures how closely the genome matches a target genome.
- **MaximizeOnesFitness**: Maximizes the number of ones in the genome.
- **MinimizeDistanceFitness**: Minimizes the distance between the genome and a target value.
- **WeightedSumFitness**: Calculates fitness as a weighted sum of genome bits.

#### 1.3 Mutation Strategies

Defined in `defaults/mutation.py`:

- **MultiElementMutation**: Mutates multiple elements in the genome based on the mutation rate.
- **ElementMutation**: Mutates a single element based on the mutation rate.
- **BitFlipMutation**: Flips genome bits based on the mutation rate.
- **SwapMutation**: Swaps two elements in the genome.
- **ScrambleMutation**: Randomly scrambles a subset of the genome.
- **SegmentSwapMutation**: Swaps two segments of the genome.
- **GaussianMutation**: Applies Gaussian mutation to genome values.
- **BoundaryMutation**: Mutates genome values within specified boundaries.
- **PolynomialMutation**: Applies polynomial mutation to genome values.

#### 1.4 Selection Strategies

Defined in `defaults/selection.py`:

- **RouletteWheelSelection**: Selects parents based on fitness proportionate probability.
- **TournamentSelection**: Selects parents using a tournament of random individuals.
- **RankSelection**: Selects parents based on rank order.
- **StochasticUniversalSampling**: Selects parents using evenly spaced fitness pointers.
- **ElitismSelection**: Selects the top `n` individuals based on fitness.
- **TruncationSelection**: Selects the top percentage of individuals.
- **BoltzmannSelection**: Selects parents using Boltzmann probabilities.
- **SteadyStateSelection**: Replaces the least fit individuals in the population.
- **RankBiasedSelection**: Selects parents using rank-based weights with a bias factor.

---

## Customization

The library allows you to define your own strategies by subclassing the provided interfaces in `strategy`.

```python
from genetic_algorithm_py.strategy import CrossoverStrategy

class CustomCrossover(CrossoverStrategy):
    def crossover(self, parent1, parent2):
        # Implement custom crossover logic here
        pass
```

---

## License

This library is licensed under the MIT License.

---

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

---

## Acknowledgments

This library was inspired by common patterns in genetic algorithms and aims to provide flexibility and usability for both academic and practical applications.
