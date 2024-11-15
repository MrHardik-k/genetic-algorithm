
# Genetic Algorithm Py Documentation

## Overview

**genetic-algorithm-py** is a Python library that provides a customizable genetic algorithm framework. It includes base classes for genetic algorithms, such as DNA representation, population management, fitness evaluation, and various selection, crossover, and mutation strategies. This library is designed for users to easily implement and test their own genetic algorithms for optimization problems.

## Table of Contents

* [Installation](#installation)
* [Getting Started](#getting-started)
* [Library Structure](#library-structure)
* [Classes and Modules](#classes-and-modules)
  * [GeneticAlgorithm](#geneticalgorithm)
  * [DNA](#dna)
  * [Individual](#individual)
  * [Population](#population)
  * [FitnessFunction](#fitnessfunction)
  * [Selection](#selection)
  * [Crossover](#crossover)
  * [Mutation](#mutation)
* [Strategies](#strategies)
  * [SelectionStrategy](#selectionstrategy)
  * [MutationStrategy](#mutationstrategy)
  * [CrossoverStrategy](#crossoverstrategy)
  * [FitnessStrategy](#fitnessstrategy)
* [Defaults](#defaults)
  * [Fitness Functions](#fitness-functions)
  * [Selection Strategies](#selection-strategies)
  * [Crossover Methods](#crossover-methods)
  * [Mutation Methods](#mutation-methods)
* [Examples](#examples)
* [Contributing](#contributing)
* [License](#license)

## Installation

To install `genetic-algorithm-py`, use:

```bash
pip install genetic-algorithm-py
```

## Getting Started

Here’s a simple example demonstrating how to create a genetic algorithm to maximize a given function.

```python
from genetic_algorithm_py import GeneticAlgorithm, DNA, Population, FitnessFunction, Selection, Crossover, Mutation
from genetic_algorithm_py.Strategy import SelectionStrategy, MutationStrategy, CrossoverStrategy

# Define a fitness function
class MyFitness(FitnessFunction):
    def evaluate(self, dna: DNA) -> float:
        # Define fitness evaluation logic here
        pass

# Initialize the population, algorithm, and other parameters
population = Population(size=100)
genetic_algo = GeneticAlgorithm(
    fitness_function=MyFitness(),
    population=population,
    selection=Selection(SelectionStrategy.TOURNAMENT),
    crossover=Crossover(CrossoverStrategy.ONE_POINT),
    mutation=Mutation(MutationStrategy.GAUSSIAN)
)

# Run the algorithm
genetic_algo.run(generations=50)
```

## Library Structure

The library is organized into modules for the core algorithm, strategies, and default implementations for fitness, selection, crossover, and mutation.

```plaintext
genetic_algorithm_py/
├── __init__.py
├── algorithm.py              # Core classes for the genetic algorithm
├── strategy/
│   ├── __init__.py
│   ├── selection_strategy.py  # Defines selection strategies
│   ├── mutation_strategy.py   # Defines mutation strategies
│   ├── crossover_strategy.py  # Defines crossover strategies
│   └── fitness_strategy.py    # Defines fitness strategies
├── defaults/
│   ├── __init__.py
│   ├── fitness_function.py    # Default fitness functions
│   ├── selection.py           # Default selection strategies
│   ├── crossover.py           # Default crossover strategies
│   └── mutation.py            # Default mutation strategies
```

## Classes and Modules

### GeneticAlgorithm

The main class for managing the algorithm's flow.

- **Attributes**:
  - `population`: Holds the population of individuals.
  - `fitness_function`: The function to evaluate fitness.
  - `selection`, `crossover`, `mutation`: Configurations for each stage of the algorithm.
- **Methods**:
  - `run(generations: int)`: Runs the algorithm for a specified number of generations.

### DNA

Represents an individual's genetic makeup.

- **Attributes**:
  - `genes`: The data representing an individual's genes.
- **Methods**:
  - `mutate()`: Applies mutation to genes.

### Individual

Represents a single individual in the population with a DNA and fitness score.

### Population

Manages a group of individuals and helps initialize, select, and manage individuals.

### FitnessFunction

Abstract class for defining fitness evaluations.

### Selection

Configures the selection process for individuals based on a strategy.

### Crossover

Defines crossover behavior based on a specified strategy.

### Mutation

Handles mutation based on the specified mutation strategy.

## Strategies

### SelectionStrategy

Available strategies include:

- **RouletteWheelSelection**: Selects individuals based on proportional fitness.
- **TournamentSelection**: Selects the best from a random subset of the population.

### MutationStrategy

- **GaussianMutation**: Mutates genes with a Gaussian distribution.
- **SwapMutation**: Swaps genes within DNA.

### CrossoverStrategy

- **OnePointCrossover**: Crosses over genes at one point.
- **UniformCrossover**: Randomly exchanges genes between parents.

### FitnessStrategy

Provides a customizable fitness function.

## Defaults

### Fitness Functions

- **MaximizeOnesFitness**: Fitness function for maximizing ones in binary genes.
- **MinimizeDistanceFitness**: Calculates the fitness based on closeness to a target.

### Selection Strategies

Default implementations for selection strategies.

### Crossover Methods

Default crossover implementations.

### Mutation Methods

Default mutation implementations.

## Examples

### Example 1: Maximize a Binary String

```python
from genetic_algorithm_py import GeneticAlgorithm, Population, DNA, FitnessFunction
from genetic_algorithm_py.defaults.fitness_function import MaximizeOnesFitness

# Initialize with MaximizeOnesFitness
fitness_function = MaximizeOnesFitness()
population = Population(size=50)
algorithm = GeneticAlgorithm(fitness_function=fitness_function, population=population)
algorithm.run(generations=30)
```

## Contributing

We welcome contributions! Please see our contribution guidelines in `CONTRIBUTING.md`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
