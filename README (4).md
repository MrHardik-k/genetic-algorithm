
# Genetic Algorithm Package

A flexible genetic algorithm implementation with customizable DNA, selection, crossover, mutation, and fitness strategies. Users can define their own strategies or use the default ones provided in the strategy folder to tailor the algorithm to specific problem domains.

## Table of Contents

- [Installation](#installation)
- [Overview](#overview)
- [Quick Start](#quick-start)
- [Classes](#classes)
  - [GeneticAlgorithm](#geneticalgorithm)
  - [DNA](#dna)
  - [Population](#population)
  - [Strategy Classes](#strategy-classes)
    - [DNAStrategy](#dnastrategy)
    - [Selection Strategies](#selection-strategies)
    - [Crossover Strategies](#crossover-strategies)
    - [Mutation Strategies](#mutation-strategies)
    - [Fitness Strategies](#fitness-strategies)
    - [Custom Strategies](#custom-strategies)

## Installation

Clone this repository and install any necessary dependencies:

```bash
git clone https://github.com/your-repo/genetic_algorithm_py.git
cd genetic_algorithm_py
```

## Overview

The genetic algorithm revolves around creating a population of genomes and evolving them through selection, crossover, mutation, and fitness evaluation. The core components include the `GeneticAlgorithm`, `DNA`, `Population`, and customizable strategy classes.

## Quick Start

To run a simple genetic algorithm with default strategies, follow this example:

```python
from genetic_algorithm_py.genetic_algorithm import GeneticAlgorithm
from genetic_algorithm_py.population import Population
from genetic_algorithm_py.dna import DNA
from genetic_algorithm_py.strategy.dna_strategy import DNAStrategy
from genetic_algorithm_py.strategy.selection_strategy import RouletteWheelSelection
from genetic_algorithm_py.strategy.crossover_strategy import HalfCrossover
from genetic_algorithm_py.strategy.mutation_strategy import ElementMutation
from genetic_algorithm_py.strategy.fitness_strategy import MaximizeOnesFitness

# Define genes and target
genes = [0, 1]
target = [1] * 10

# Set up DNAStrategy with default strategies
dna_strategy = DNAStrategy(
    genes=genes,
    target=target,
    selection_strategy=RouletteWheelSelection(),
    crossover_strategy=HalfCrossover(),
    mutation_strategy=ElementMutation(),
    fitness_strategy=MaximizeOnesFitness()
)

# Initialize DNA with the DNAStrategy
dna = DNA(dna_strategy)

# Create a population
population = Population(dna=dna, size=100, genome_length=len(target))

# Run the Genetic Algorithm
ga = GeneticAlgorithm(dna=dna, population_size=100, genome_size=len(target), mutation_rate=0.01)
ga.run(num_generations=50)
```

## Classes

### GeneticAlgorithm

The `GeneticAlgorithm` class is responsible for evolving the population. It uses the `DNA`, `Population`, and `DNAStrategy` classes to apply selection, crossover, mutation, and fitness strategies.

- **Parameters**
  - `dna`: Instance of the DNA class, configured with a specific DNAStrategy.
  - `population_size`: Number of individuals in the population.
  - `genome_size`: Length of each genome.
  - `mutation_rate`: Probability of mutation per gene.

### DNA

The `DNA` class manages genetic operations by using a `DNAStrategy` that defines how selection, crossover, mutation, and fitness evaluation are handled.

- **Parameters**
  - `dna_strategy`: An instance of `DNAStrategy`.

### Population

The `Population` class initializes a population based on the provided DNA and genome size.

- **Parameters**
  - `dna`: Instance of the DNA class.
  - `size`: Population size.
  - `genome_length`: Length of each genome.

## Strategy Classes

### DNAStrategy

The `DNAStrategy` class manages the genetic operations required by the DNA class. By default, it provides:

- `RouletteWheelSelection` for selection
- `HalfCrossover` for crossover
- `ElementMutation` for mutation
- `MaximizeOnesFitness` for fitness evaluation

#### Example

```python
dna_strategy = DNAStrategy(
    genes=[0, 1],
    target=[1] * 10,
    selection_strategy=RouletteWheelSelection(),
    crossover_strategy=HalfCrossover(),
    mutation_strategy=ElementMutation(),
    fitness_strategy=MaximizeOnesFitness()
)
```

### Selection Strategies

Selection strategies define how individuals are selected for reproduction. Available strategies:

- `RouletteWheelSelection`: Selects based on relative fitness probabilities.
- `TournamentSelection`: Selects top individuals after competing in a "tournament" of random pairs.

#### Example

```python
from genetic_algorithm_py.strategy.selection_strategy import TournamentSelection

dna_strategy = DNAStrategy(
    genes=[0, 1],
    selection_strategy=TournamentSelection()
)
```

### Crossover Strategies

Crossover strategies define how genes are combined from two parents. Available strategies:

- `HalfCrossover`: Combines half of each parent's genes.
- `UniformCrossover`: Randomly chooses genes from either parent.

#### Example

```python
from genetic_algorithm_py.strategy.crossover_strategy import UniformCrossover

dna_strategy = DNAStrategy(
    genes=[0, 1],
    crossover_strategy=UniformCrossover()
)
```

### Mutation Strategies

Mutation strategies define how genes are altered randomly. Available strategies:

- `ElementMutation`: Randomly mutates individual elements in the genome.

#### Example

```python
from genetic_algorithm_py.strategy.mutation_strategy import ElementMutation

dna_strategy = DNAStrategy(
    genes=[0, 1],
    mutation_strategy=ElementMutation()
)
```

### Fitness Strategies

Fitness strategies define the fitness evaluation of genomes. Available strategies:

- `MaximizeOnesFitness`: Scores genomes based on the number of 1s.
- `TargetMatchFitness`: Scores genomes based on similarity to a target.

#### Example

```python
from genetic_algorithm_py.strategy.fitness_strategy import TargetMatchFitness

dna_strategy = DNAStrategy(
    genes=[0, 1],
    fitness_strategy=TargetMatchFitness(target=[1] * 10)
)
```

### Custom Strategies

To create a custom strategy, subclass any strategy base class and override necessary methods. Here’s an example of a custom selection strategy:

```python
from genetic_algorithm_py.strategy.selection_strategy import SelectionStrategy

class CustomSelection(SelectionStrategy):
    def select(self, population):
        # Custom selection logic
        pass

# Use the custom strategy
dna_strategy = DNAStrategy(
    genes=[0, 1],
    selection_strategy=CustomSelection()
)
```
