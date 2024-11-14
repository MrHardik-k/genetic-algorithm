from ..individual import Individual
from ..population import Population

class SelectionStrategy:
    def select_parents(self, population:Population)->tuple[Individual, Individual]:
        raise NotImplementedError("This method should be overridden by subclasses")
