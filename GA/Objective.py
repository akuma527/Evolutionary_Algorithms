import numpy as np 
 

class objective_function():


    def __init__(self):
        return

    # to find the maximum of this function
    def objective(self, x):
        return np.sin(10*x)*x + np.cos(2*x)*x


ob = objective_function()
print(ob.objective(x=10))