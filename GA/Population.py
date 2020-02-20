import numpy as np 

class Population():


    def __init__(self, candidates, dimensions, lb=0, ub=1):
        self.candidates = candidates
        self.dimensions = dimensions
        self.lb = lb
        self.ub = ub

    def generate_pop(self):
        pop = np.random.rand(self.candidates, self.dimensions)
        if ((self.lb!=0) or (self.ub!=1)):
            scale = (self.ub - self.lb)
            pop = self.lb + pop*scale
        return pop



ob = Population(candidates=3, dimensions=2, lb=1,ub=5)
pop = ob.generate_pop()

print(pop)