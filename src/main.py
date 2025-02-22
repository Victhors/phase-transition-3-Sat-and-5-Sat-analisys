import random
from pysat.solvers import Solver
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import time
from analisar_transicao_de_fase import (
    analisar_transicao_de_fase,
)
from gerar_plots import (
    plot_results,
    plot_execution_times,
)

def main():

    try:

        # Parâmetros para a análise
        n_values_3sat = [50, 100, 150, 200] # numero de instancias por clausula no 3-SAT
        n_values_5sat = [20, 30, 40, 50] # numero de instancias por clausula no 5-SAT
        k_3sat = 3 # numero de literais por clausula no 3-SAT
        k_5sat = 5 # numero de literais por clausula no 5-SAT
        alpha_range_3sat = [i * 0.1 for i in range(10, 101)]  # α de 1 a 10
        alpha_range_5sat = [i * 0.1 for i in range(10, 301)]  # α de 1 a 30

        print("Iniciando análise 3-SAT...")
        results_3sat, execution_times_3sat = analisar_transicao_de_fase(n_values_3sat, k_3sat, alpha_range_3sat)
        plot_results(results_3sat, alpha_range_3sat, k_3sat, n_values_3sat)
        plot_execution_times(execution_times_3sat, alpha_range_3sat, k_3sat, n_values_3sat)

        print("Iniciando análise 5-SAT...")
        results_5sat, execution_times_5sat = analisar_transicao_de_fase(n_values_5sat, k_5sat, alpha_range_5sat)
        plot_results(results_5sat, alpha_range_5sat, k_5sat, n_values_5sat)
        plot_execution_times(execution_times_5sat, alpha_range_5sat, k_5sat, n_values_5sat)
        
        print("Análise completa! Os gráficos foram salvos na pasta plots.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()