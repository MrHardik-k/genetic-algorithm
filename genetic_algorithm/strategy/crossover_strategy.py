# from typing import TYPE_CHECKING
# if TYPE_CHECKING:
#     from ..algorithm import Individual
from ..individual import Individual
from ..population import Population

class CrossoverStrategy:
    def crossover(self, parent1:Individual, parent2:Individual)->tuple[Individual, Individual]:
        raise NotImplementedError("This method should be overridden by subclasses")
