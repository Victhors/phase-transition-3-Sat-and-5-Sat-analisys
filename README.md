# Análise de Transição de Fase para 3-SAT e 5-SAT

## Geração de Instâncias (`gerar_instancia_sat.py`)

- Gera instâncias aleatórias de k-SAT com n variáveis e m cláusulas.
- Cada cláusula possui k literais únicos sem contradições (ex.: ¬x v y em 3-SAT).
- O parâmetro alpha (m/n) varia de 1 a 10 para 3-SAT e de 1 a 30 para 5-SAT, explorando a região crítica de transição de fase.

## Resolução de SAT (`isso_e_satisfazivel.py`)

- Utiliza o solver Glucose3 da biblioteca PySAT para determinar a satisfazibilidade.
- Retorna um booleano indicando se a instância é satisfazível (`True/False`).

## Análise de Transição (`analisar_transicao_de_fase.py`)

- Avalia 30 instâncias por valor de alpha para estatísticas robustas.
- Registra para o 3-SAT:
	- Probabilidade de satisfatibilidade (gráfico `phase_transition_3sat.png/5sat.png`).
	- Tempo de execução (gráfico `execution_time_3sat.png/5sat.png`).
- Registra para o 5-SAT:
	- Probabilidade de satisfatibilidade (gráfico `phase_transition_3sat.png/5sat.png`).
	- Tempo de execução (gráfico `execution_time_3sat.png/5sat.png`).
- Valores de n testados:
	- **3-SAT**: n = {50, 100, 150, 200}.
	- **5-SAT**: n = {20, 30, 40, 50} (devido à complexidade computacional).

## Resultados

### 3-SAT

- **Transição de Fase**: A probabilidade de satisfazibilidade cai abruptamente em alpha entre 4,2-4,3.
- **Complexidade Computacional**: O tempo de execução aumenta exponencialmente próximo a alpha = 4,2 , refletindo a região crítica.
-  Esses resultados alinham-se especificadamente com as teorias de (Mezard et al. 2002) e (Selman et al. 2021): 
	-   *"Survey propagation (SP) up till 4.2 (empirical, Mezard, Parisi, Zecchina ’02) approx. 1,000,000 vars near phase transition."*  (Selman et al. 2021)


### 5-SAT

- **Transição de Fase**: A transição ocorre em alpha entre 21-22, significativamente mais alto que o 3-SAT.
- **Complexidade Computacional**: Requer valores menores de n para observar a transição devido à complexidade intrínseca do problema (k = 5).

## Comparação entre 3-SAT e 5-SAT

### Principais diferenças:

1. **Localização da Transição de Fase:**

   - 3-SAT transita em um alpha menor (aproximadamente 4,2)
   - 5-SAT transita em um alpha maior (aproximadamente 21)

2. **Acentuação da Transição:**

   - 5-SAT apresenta uma transição mais abrupta
   - 3-SAT tem uma mudança mais gradual

3. **Complexidade Computacional:**

   - 5-SAT requer valores menores de n devido à maior complexidade
   - Os tempos de execução aumentam de forma mais dramática com n para o 5-SAT

| Característica           | 3-SAT                       | 5-SAT                           |
| ------------------------ | --------------------------- | ------------------------------- |
| **Transição de Fase**    | alpha 4,2 (transição suave) | alpha 21 (transição abrupta)    |
| **Complexidade**         | Menor sensibilidade a n     | Tempo de execução explode com n |
| **Tamanho de Instância** | n maior (50-200)            | n menor (10-40)                 |

### Grafico do Tempo de Execução do 3-SAT

![3-SAT-time.png|600](https://i.imgur.com/xC7XOOB.png)

### Grafico do Tempo de Execução do 5-SAT 

![5-SAT-time.png|600](https://i.imgur.com/cSBEB74.png)


### Grafico da Probabilidade de Satisfazibilidade do 3-SAT

![3-SAT-prob.png|600](https://i.imgur.com/xRGySOD.png)


### Grafico da Probabilidade de Satisfazibilidade do 5-SAT

![5-SAT-prob.png|600](https://i.imgur.com/VGYrNR0.png)


### Interpretação:

- Maiores valores de k (ex.: 5-SAT) intensificam a complexidade, resultando em transições mais abruptas e maiores alpha críticos.
- O 5-SAT exige otimizações computacionais avançadas para escalabilidade.

## Referências

- Mezard, M., Parisi, R., & Zecchina, R. (2002). "Random k-satisfiability problem: From an analytic solution to an efficient algorithm." Physical Review E, 66(5), 056126
- Selman, B. (2021). The Next Generation of Automated Reasoning Methods. Lecture Notes for CS6700, Cornell University, Spring 2021.
  Disponível em: https://www.cs.cornell.edu/courses/cs6700/2021sp/lectures/CS6700-05-SAT_physics_structure_update_v3.pdf

