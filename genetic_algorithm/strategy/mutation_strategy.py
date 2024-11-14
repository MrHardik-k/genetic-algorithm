from ..individual import Individual

class MutationStrategy:
    def __init__(self, mutation_rate:float=0.01):
        self.mutation_rate = mutation_rate

    def mutate(self, individual:Individual)->Individual:
        """This method should be overridden by specific mutation strategies."""
        raise NotImplementedError("Mutation strategy must implement the mutate method.")