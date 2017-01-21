# Creates a list of the Ingredients
Ingredients = ['CHICKEN', 'BEEF', 'MUTTON', 'RICE', 'WHEAT', 'GEL']

# A dictionary of the costs of each of the Ingredients is created
costs = {'CHICKEN': 0.013, 
         'BEEF': 0.008, 
         'MUTTON': 0.010, 
         'RICE': 0.002, 
         'WHEAT': 0.005, 
         'GEL': 0.001}

# A dictionary of the protein percent in each of the Ingredients is created
proteinPercent = {'CHICKEN': 0.100, 
                  'BEEF': 0.200, 
                  'MUTTON': 0.150, 
                  'RICE': 0.000, 
                  'WHEAT': 0.040, 
                  'GEL': 0.000}

for key, value in proteinPercent.items():
    proteinPercent[key] = -1.0*value

# A dictionary of the fat percent in each of the Ingredients is created
fatPercent = {'CHICKEN': 0.080, 
              'BEEF': 0.100, 
              'MUTTON': 0.110, 
              'RICE': 0.010, 
              'WHEAT': 0.010, 
              'GEL': 0.000}

for key, value in fatPercent.items():
    fatPercent[key] = -1.0*value

# A dictionary of the fibre percent in each of the Ingredients is created
fibrePercent = {'CHICKEN': 0.001, 
                'BEEF': 0.005, 
                'MUTTON': 0.003, 
                'RICE': 0.100, 
                'WHEAT': 0.150, 
                'GEL': 0.000}

# A dictionary of the salt percent in each of the Ingredients is created
saltPercent = {'CHICKEN': 0.002, 
               'BEEF': 0.005, 
               'MUTTON': 0.007, 
               'RICE': 0.002, 
               'WHEAT': 0.008, 
               'GEL': 0.000}

Percents = [proteinPercent, fatPercent, fibrePercent, saltPercent]

import numpy as np
from cvxopt import matrix, solvers, printing
printing.options['dformat'] = '%.4f'
#solvers.options['show_progress'] = False #for default
#solvers.options['glpk'] = {'msg_lev': 'GLP_MSG_OFF'}

c = matrix([costs[i] for i in Ingredients])
N = np.transpose(np.array([j[i] for i in Ingredients for j in Percents]).reshape(len(Ingredients), len(Percents)))
N =  np.concatenate((N, np.zeros((12, 6), dtype = float)), axis = 0)
j = 0
for i in range(4, 15, 2):
    N[i, j] = 1.
    N[i + 1, j] = -1.
    j += 1
G = matrix(N)
h = matrix([-8., -6., 2., 0.4] + [100., 0.]*6)
A = matrix([[1.],[1.],[1.],[1.],[1.],[1.]])
b = matrix([100.])
sol = solvers.lp(c, G, h, A, b, solver='glpk')
print(sol['x'])
print(sol['primal objective'])
