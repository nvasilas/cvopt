import pulp
def lp_pulp():
    my_lp_problem = pulp.LpProblem("My LP Problem", pulp.LpMaximize)
    x = pulp.LpVariable('x', lowBound=0, cat='Continuous')
    y = pulp.LpVariable('y', lowBound=2, cat='Continuous')
    # Objective function
    my_lp_problem += 4 * x + 3 * y, "Z"
    # Constraints
    my_lp_problem += 2 * y <= 25 - x
    my_lp_problem += 4 * y >= 2 * x - 8
    my_lp_problem += y <= 2 * x - 5
    my_lp_problem.solve()
    return my_lp_problem

sol = lp_pulp()
if pulp.LpStatus[sol.status] == "Optimal":
    for variable in sol.variables():
        print("{} = {}".format(variable.name, variable.varValue))
    print("objective value = ", pulp.value(sol.objective))
