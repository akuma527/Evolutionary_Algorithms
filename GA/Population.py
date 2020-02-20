import numpy as np 

class Population():


    def __init__(self, candidates, dimensions, lb=0, ub=1, seed=None):
        self.candidates = candidates
        self.dimensions = dimensions
        self.lb = lb
        self.ub = ub
        self.seed = seed

    def generate_pop(self):
        if self.seed:
            np.random.seed(self.seed)
        
        pop = np.random.rand(self.candidates, self.dimensions)
        
        if ((self.lb!=0) or (self.ub!=1)):
            scale = (self.ub - self.lb)
            pop = self.lb + pop*scale
        return pop



ob = Population(candidates=3, dimensions=2, lb=1,ub=5, seed=1)
pop = ob.generate_pop()

print(pop)