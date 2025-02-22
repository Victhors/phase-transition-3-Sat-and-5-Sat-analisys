import random
from pysat.solvers import Solver
import matplotlib
matplotlib.use('Agg')  # Set non-interactive backend
import matplotlib.pyplot as plt
from gerar_instancia_sat import gerar_instancia_sat
from isso_e_satisfazivel import isso_e_satisfazivel
import time

def analisar_transicao_de_fase(n_valores, k, alpha_range, numero_de_instancias=30):
    """
    Analisa a transição de fase para k-SAT, variando alpha em um intervalo.
    
    Args:
        n_valores (list): Lista de valores de n a serem analisados.
        k (int): Número de literais por cláusula (3 para 3-SAT, 5 para 5-SAT).
        alpha_range (list): Lista de valores de alpha.
        num_instances (int): Número de instâncias por valor de alpha.
    
    Returns:
        tuple: Dicionários contendo probabilidades de satisfazibilidade e tempos de execução.
    """
    resultados = {}
    tempos_execucao = {}

    for n in n_valores:
        resultados[n] = []
        tempos_execucao[n] = []
        for alpha in alpha_range:
            m = int(alpha * n)
            contador_satisfazivel = 0
            tempo_total = 0

            for _ in range(numero_de_instancias):
                instancia = gerar_instancia_sat(n, m, k)
                tempo_inicial = time.time()
                if isso_e_satisfazivel(instancia):
                    contador_satisfazivel += 1
                tempo_final = time.time()
                tempo_total += tempo_final - tempo_inicial

            probabilidade = contador_satisfazivel / numero_de_instancias
            tempo_medio = tempo_total / numero_de_instancias

            resultados[n].append(probabilidade)
            tempos_execucao[n].append(tempo_medio)

    return resultados, tempos_execucao

