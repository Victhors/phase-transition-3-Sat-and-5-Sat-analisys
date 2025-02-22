import random
from operator import abs as abs_op

def validar_parametros(n, m, k):
    if n < k or n < m:
        return "numero de variaveis menor que o numero de literais por clausula ou menor que o numero de clausulas"
    if m < 1:
        return "numero de clausulas menor que 1"
    if k < 1:
        return "numero de literais por clausula menor que 1"
    return None

def gerar_clausulas_aleatorias(n, k, clausulas_existentes=None):
    """
    Gera uma cláusula aleatória com k literais distintos, sem repetições ou literais contraditórios,
    evitando duplicações se receber um conjunto de cláusulas já existentes.
    """
    if clausulas_existentes is None:
        clausulas_existentes = set()
    while True:
        variables = random.sample(range(1, n + 1), k)
        signs = [random.choice([-1, 1]) for _ in range(k)]
        clause = [signs[i] * variables[i] for i in range(k)]
        normalized = tuple(sorted(clause, key=lambda x: abs_op(x)))
        if normalized not in clausulas_existentes:
            clausulas_existentes.add(normalized)
            return clause

def gerar_instancia_sat(n, m, k):
    """
    Gera uma instância aleatória de k-SAT com n variáveis e m cláusulas.
    
    Args:
        n (int): Número de variáveis.
        m (int): Número de cláusulas.
        k (int): Número de literais por cláusula.
    
    Returns:
        list: Uma lista de cláusulas representando a instância.
    """
    validar_parametros(n, m, k)
    instancia = []
    for _ in range(m):
        clause = gerar_clausulas_aleatorias(n, k)
        instancia.append(clause)
    return instancia
