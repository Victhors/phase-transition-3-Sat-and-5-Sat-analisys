from pysat.solvers import Solver

def isso_e_satisfazivel(instance):
    """
    Verifica se uma instância k-SAT é satisfazível usando PySAT.
    """
    
    solver = Solver(name='glucose3')
    for clause in instance:
        solver.add_clause(clause)
    return solver.solve()
    
    