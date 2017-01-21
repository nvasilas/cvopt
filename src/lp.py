def graph_lp_cvxopt():
    import numpy as np
    import matplotlib.pyplot as plt
    # x > 0
    x = np.linspace(0, 20, 2000)
    # y >= 2
    y1 = (x*0) + 2
    # 2y <= 25 - x
    y2 = (25-x)/2.0
    # 4y >= 2x - 8 
    y3 = (2*x-8)/4.0
    # y <= 2x - 5 
    y4 = 2 * x -5

    plt.plot(x, y2, label=r'$x + 2y\leq 25$')
    plt.plot(x, y3, label=r'$2x - 4y \leq 8$')
    plt.plot(x, y4, label=r'$-2x + y\leq -5$')
    plt.plot(x, y1, label=r'$-y\leq-2$')
    plt.xlim((0, 16))
    plt.ylim((0, 11))
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    y5 = np.minimum(y2, y4)
    y6 = np.maximum(y1, y3)
    plt.fill_between(x, y5, y6, where=y5>y6, color='grey', alpha=0.5)
    plt.legend(loc='best')
    return plt

def lp_cvxopt():
    from cvxopt import matrix, solvers, printing
    printing.options['dformat'] = '%.4f'
    #solvers.options['show_progress'] = False #for default
    solvers.options['glpk'] = {'msg_lev': 'GLP_MSG_OFF'}
    # matrix creates by column
    c = matrix([-4., -3.])
    G = matrix([[1., 2., -2., -1., 0.], [2., -4., 1., 0., -1]])
    h = matrix([25., 8., -5., 0., -2.])
    sol = solvers.lp(c, G, h, solver='glpk')
    return sol

sol = lp_cvxopt() 
try:
    if sol['status'] == "optimal":
        print(sol['x'])
        print("objective value = ", -sol['primal objective'])

        plt = graph_lp_cvxopt()
        from matplotlib import rcParams
        rcParams['font.family'] = "Kerkis"
        rcParams['text.usetex'] = True
        rcParams['text.latex.unicode'] = True
        plt.plot(sol['x'][0], sol['x'][1], 'or')
        plt.grid()
        plt.savefig('lp2.png')
        plt.show()
except NameError:
    pass

def lp_mat_ex1():
    from cvxopt import matrix, solvers, printing
    printing.options['dformat'] = '%.4f'
    #solvers.options['show_progress'] = False #for default
    solvers.options['glpk'] = {'msg_lev': 'GLP_MSG_OFF'}
    c = matrix([-1., -1./3.])
    G = matrix([[1., 1., 1., -1./4., -1., -1], [1., 1./4., -1., -1., -1., 1.]])
    print(G)
    h = matrix([2., 1., 2., 1., -1., 2.])
    #solvers.options['show_progress'] = False #for default
    solvers.options['glpk'] = {'msg_lev': 'GLP_MSG_OFF'}
    sol = solvers.lp(c, G, h, solver='glpk')
    return sol

def lp_mat_ex2():
    from cvxopt import matrix, solvers, printing
    printing.options['dformat'] = '%.4f'
    #solvers.options['show_progress'] = False #for default
    solvers.options['glpk'] = {'msg_lev': 'GLP_MSG_OFF'}

    c = matrix([-1., -1./3.])
    G = matrix([[1., 1., 1., -1./4., -1., -1], [1., 1./4., -1., -1., -1., 1.]])
    h = matrix([2., 1., 2., 1., -1., 2.])
    A = matrix([[1.], [1./4.]])
    b = matrix([1./2.])
    #solvers.options['show_progress'] = False #for default
    solvers.options['glpk'] = {'msg_lev': 'GLP_MSG_OFF'}
    sol = solvers.lp(c, G, h, A, b, solver='glpk')
    return sol

def graph_lp_mat_ex3():
    import numpy as np
    import matplotlib.pyplot as plt
    x = np.linspace(-1., 1.5, 200)
    y1 = 2 - x
    y2 = 4*(1 - x)
    y3 = x - 2
    y4 = 1/4*x - 1
    y5 = 1 - x
    y6 = 2 + x
    y7 = 2 - 4*x
    y8 = -0.5 + 0*x
    y9 = 1.25 + 0*x

    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.plot(x, y3)
    plt.plot(x, y4)
    plt.plot(x, y5)
    plt.plot(x, y6)
    plt.plot(x, y7)
    plt.plot(x, y8)
    plt.plot(x, y9)
    #plt.xlim((0, 16))
    #plt.ylim((0, 11))
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    #y5 = np.minimum(y2, y4)
    #y6 = np.maximum(y1, y3)
    #plt.fill_between(x, y5, y6, where=y5>y6, color='grey', alpha=0.5)
    plt.legend(loc='best')
    return plt

def lp_mat_ex3():
    from cvxopt import matrix, solvers, printing
    printing.options['dformat'] = '%.4f'
    #solvers.options['show_progress'] = False #for default
    solvers.options['glpk'] = {'msg_lev': 'GLP_MSG_OFF'}

    c = matrix([-1., -1./3.])
    G = matrix([[1., 1., 1., -1./4., -1., -1., 1., -1., 0., 0.], \
            [1., 1./4., -1., -1., -1., 1., 0., 0., 1., -1.]])
    h = matrix([2., 1., 2., 1., -1., 2., 1.5, 1., 1.25, 0.5])
    A = matrix([[1.], [1./4.]])
    b = matrix([1./2.])
    #solvers.options['show_progress'] = False #for default
    solvers.options['glpk'] = {'msg_lev': 'GLP_MSG_OFF'}
    sol = solvers.lp(c, G, h, A, b, solver='glpk')
    return sol

#sol3 = lp_mat_ex3() 
try:
    if sol3['status'] == "optimal":
        print(sol3['x'])
        print("objective value = ", sol3['primal objective'])

        plt = graph_lp_mat_ex3()
        from matplotlib import rcParams
        rcParams['font.family'] = "Kerkis"
        rcParams['text.usetex'] = True
        rcParams['text.latex.unicode'] = True
        plt.plot(sol3['x'][0], sol3['x'][1], 'or')
        plt.show()
except NameError:
    pass

