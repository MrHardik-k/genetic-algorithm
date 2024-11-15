
# Genetic Algorithm Library

This Python library, `genetic_algorithm_py`, provides a flexible framework for implementing genetic algorithms, featuring customizable strategies for selection, crossover, mutation, and fitness evaluation. The library enables users to create, manage, and evolve populations of individuals represented by genomes composed of genes.

## Table of Contents
- [Installation](#installation)
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Class Descriptions](#class-descriptions)
  - [Individual](#individual)
  - [Population](#population)
  - [Strategy Classes](#strategy-classes)
    - [SelectionStrategy](#selectionstrategy)
    - [CrossoverStrategy](#crossoverstrategy)
    - [MutationStrategy](#mutationstrategy)
    - [FitnessStrategy](#fitnessstrategy)
  - [DNAStrategy](#dnastrategy)
- [Examples](#examples)
- [Future Extensions](#future-extensions)

## Installation

Clone this repository and install required packages if any (e.g., `random` is part of Python’s standard library). Ensure that Python 3.9 or later is installed to support type hinting for `tuple[Individual, Individual]`.

```bash
pip install genetic_algorithm_py
```

## Overview

Genetic algorithms (GAs) are optimization techniques inspired by natural evolution. This library uses an object-oriented approach to implement customizable genetic algorithms, providing base classes for different genetic operations. Subclass these base classes to define specific strategies or use the default implementations available in the `defaults` package.

## Project Structure

```plaintext
genetic_algorithm_py/
├── algorithm/
│   ├── selection.py
│   ├── crossover.py
│   ├── mutation.py
│   └── fitness_function.py
├── strategy/
│   ├── __init__.py
│   ├── crossover_strategy.py
│   ├── dna_strategy.py
│   ├── fitness_strategy.py
│   ├── mutation_strategy.py
│   └── selection_strategy.py
├── individual.py
├── population.py
└── README.md
```

## Usage

1. **Define or Customize Strategies**: Extend any strategy classes in the `strategy` folder to create custom genetic operations.
2. **Set Up the Algorithm**: Use the `DNAStrategy` class to specify genes, target genomes, and select the strategies for selection, crossover, mutation, and fitness evaluation.
3. **Run the Algorithm**: Instantiate `Population` with a set of individuals and use the strategies to evolve generations.

## Class Descriptions

### Individual
Represents a single member of the population with a genome and associated fitness.

- **Attributes**
  - `genome`: A list of genes representing the individual.
  - `fitness`: A float representing the individual's fitness score.
  
- **Methods**
  - `update_fitness()`: Recalculate fitness based on the provided fitness strategy.

### Population
Represents a collection of individuals in the genetic algorithm.

- **Attributes**
  - `individuals`: A list of `Individual` objects.

- **Methods**
  - `evaluate_population()`: Calculates the fitness of each individual using the fitness strategy.
  - `select()`, `crossover()`, `mutate()`: Performs genetic operations on the population using the chosen strategies.

### Strategy Classes

Each strategy class defines a specific operation in the genetic algorithm. Subclass these for custom behavior.

#### SelectionStrategy
Defines the method for selecting parents from the population.

- **Methods**
  - `select_parents(population)`: Abstract method; overridden in subclasses to select two parents.

#### CrossoverStrategy
Handles recombination of parent genomes to produce offspring.

- **Methods**
  - `crossover(parent1, parent2)`: Abstract method; overridden in subclasses to define specific crossover behavior.

#### MutationStrategy
Defines how individual genomes mutate to introduce genetic variation.

- **Methods**
  - `mutate(individual)`: Abstract method; overridden in subclasses to define mutation behavior.

#### FitnessStrategy
Evaluates the fitness of an individual based on its genome.

- **Methods**
  - `evaluate(genome)`: Abstract method; overridden in subclasses to calculate fitness.

### DNAStrategy
A higher-level strategy class that combines the selection, crossover, mutation, and fitness strategies to dictate genetic algorithm behavior.

- **Attributes**
  - `genes`: A list of possible genes for creating genomes.
  - `target`: An optional target genome used for fitness comparisons.
  - `duplicate_genomes`: Boolean indicating if duplicate genes are allowed in genomes.
  
- **Methods**
  - `generate_genome(genome_size)`: Generates a genome of the specified size, with or without duplicates.
  - `get_random_genes(genes_size)`: Retrieves a random selection of genes.
  
- **Exceptions**
  - `__init_subclass__()`: Prevents subclasses from overriding the `__init__` method.

## Examples

### Example 1: Using Default Strategies

```python
from genetic_algorithm_py.individual import Individual
from genetic_algorithm_py.population import Population
from genetic_algorithm_py.strategy.dna_strategy import DNAStrategy

# Define genes and create a DNA strategy instance with default behaviors
genes = [0, 1]
dna_strategy = DNAStrategy(genes)

# Create a population with 10 individuals and initialize genomes
population = Population([Individual(dna_strategy.generate_genome(5)) for _ in range(10)])
population.evaluate_population()
```

### Example 2: Custom Crossover Strategy

```python
from genetic_algorithm_py.strategy.crossover_strategy import CrossoverStrategy

# Custom crossover that swaps halves of genomes
class CustomCrossover(CrossoverStrategy):
    def crossover(self, parent1, parent2):
        mid = len(parent1.genome) // 2
        child1_genome = parent1.genome[:mid] + parent2.genome[mid:]
        child2_genome = parent2.genome[:mid] + parent1.genome[mid:]
        return Individual(child1_genome), Individual(child2_genome)

# Use CustomCrossover in the DNAStrategy
dna_strategy.crossover_strategy = CustomCrossover()
```

## Future Extensions

This library provides a robust base for creating genetic algorithms, but additional functionality could further enhance it:

1. **Additional Genetic Operations**: Create more specific strategies, such as tournament selection or uniform crossover.
2. **Parallel Evaluation**: Use multiprocessing to evaluate large populations more efficiently.
3. **Logging and Visualization**: Implement logging for tracking generations and fitness over time, as well as visualization of progress.

This genetic algorithm library is modular and extensible, making it easy to experiment with different evolutionary strategies and configurations for various optimization tasks. Enjoy exploring the possibilities!
