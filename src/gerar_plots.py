import os
import matplotlib
matplotlib.use('Agg')  # Set non-interactive backend
import matplotlib.pyplot as plt

def garantir_que_a_pasta_plot_existe():
    plots_dir = "plots"
    if not os.path.exists(plots_dir):
        os.makedirs(plots_dir)
    return plots_dir

def plot_results(results, alpha_range, k, n_values):
    """
    Plota e salva a probabilidade de satisfazibilidade em função de alpha.
    """
    plots_dir = garantir_que_a_pasta_plot_existe()
    plt.figure(figsize=(10, 6))
    for n in n_values:
        plt.plot(alpha_range, results[n], label=f'n={n}')
    plt.xlabel('α (cláusulas/variáveis)')
    plt.ylabel('Probabilidade de Satisfazibilidade')
    plt.title(f'Transição de Fase para {k}-SAT')
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(plots_dir, f'phase_transition_{k}sat.png'))
    plt.close()

def plot_execution_times(execution_times, alpha_range, k, n_values):
    """
    Plota e salva o tempo médio de execução em função de alpha.
    """
    plots_dir = garantir_que_a_pasta_plot_existe()
    plt.figure(figsize=(10, 6))
    for n in n_values:
        plt.plot(alpha_range, execution_times[n], label=f'n={n}')
    plt.xlabel('α (cláusulas/variáveis)')
    plt.ylabel('Tempo Médio de Execução (s)')
    plt.title(f'Tempo de Execução para {k}-SAT')
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(plots_dir, f'execution_time_{k}sat.png'))
    plt.close()