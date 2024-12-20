### Exercise 5.1

Consider the diagrams on the right in Figure 5.1. Why does the estimated value function jump up for the last two rows in the rear? Why does it drop off for the whole last row on the left? Why are the frontmost values higher in the upper diagrams than in the lower?

![alt text](image-3.png)

В конце графиков у игрока на руке 20 и 21 и он перестаёт брать карты. С такой суммой шанс выигрыша будет выше, чем с 19 и меньше.

В левой части график спадает, так как у дилера есть туз, который может использоваться как 1, что даёт шансы дилеру на победу.

С используемым тузом у игрока снижаются шансы на проигрыш из-за перебора.

### Exercise 5.2

Suppose every-visit MC was used instead of first-visit MC on the blackjack task. Would you expect the results to be very different? Why or why not?

Использование Every-visit означает, что значение туза сменяется с 11 до 1. Такие случаи не должны происходить часто, так что результаты не должы сильно отличаться.

### Exercise 5.3

What is the backup diagram for Monte Carlo estimation of $q_\pi$?

Диаграммы по структуре аналогичный диаграмме для функции $V_{\pi}(s)$, которая строится по Монте Карло. Только здесь также появляются вершины, обозначающие выбранное действие.

### Exercise 5.4

The pseudocode for Monte Carlo ES is ineffcient because, for each state–action pair, it maintains a list of all returns and repeatedly calculates their mean. It would be more effcient to use techniques similar to those explained in Section 2.4 to maintain just the mean and a count (for each state–action pair) and update them incrementally. Describe how the pseudocode would be altered to achieve this.

Для решения этой проблемы будем подсчитывать количество элементов, взятых в усреднении и делать соответствующее инкрементирование:

Сперва увеличиваем счётчик $N$, потом:

$$
    Q(S_t,A_t) = Q(S_t,A_t) + \dfrac{1}{N}(G - Q(S_t,A_t))
$$

### Exercise 5.5

Consider an MDP with a single nonterminal state and a single action that transitions back to the nonterminal state with probability p and transitions to the terminal state with probability 1-p. Let the reward be +1 on all transitions, and let γ = 1. Suppose you observe one episode that lasts 10 steps, with a return of 10. What are the first-visit and every-visit estimators of the value of the nonterminal state

Представим этот эпизод в виде таблицы

| шаг | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| состояние | s | s | s | s | s | s | s | s | s | s | T |
| награда | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 |
| действие | p | p | p | p | p | p | p | p | p | 1 - p | - |

Для first-visit получим

$$
    V(s) = \dfrac{10}{1} = 10
$$

Для every-visit получим

$$
    V(s) = \dfrac{1 + 2 + \dots + 10}{10} = 5.5   
$$

### Exercise 5.6

What is the equation analogous to (5.6) for action values q(s, a) instead of state values v(s), again given returns generated using b?

Формула (5.6):

$$
    V(s) = \dfrac{\sum\limits_{t\in\mathcal{T}(s)}\rho_{t:T(t)-1}G_t}{\sum\limits_{t\in\mathcal{T}(s)}\rho_{t:T(t)-1}}
$$

Добавим аргумент выбора действия

$$
    Q(s, a) = \dfrac{\sum\limits_{t\in\mathcal{T}(s, a)}\rho_{t:T(t)-1}G_t}{\sum\limits_{t\in\mathcal{T}(s, a)}\rho_{t:T(t)-1}}
$$

Распишем $\rho$

$$
    Q(s, a) = \dfrac{\sum\limits_{t\in\mathcal{T}(s, a)}\prod\limits_{k=t}^{T-1}\dfrac{\pi(A_k|S_k)}{b(A_k|S_k)} G_t}{\sum\limits_{t\in\mathcal{T}(s, a)}\prod\limits_{k=t}^{T-1}\dfrac{\pi(A_k|S_k)}{b(A_k|S_k)}}
$$

При оценке $Q(s,a)$ мы в первую очередь интересуемся тем, чтобы оценить функцию при принятии действия $a_t$ в состоянии $s_t$ в момент времени $t$, поэтому нам не важно, какой стратегией мы выбрали данное действие, поэтому положим, что 

$$
    \pi(A_t=a|S_t=s)=1, \; b(A_t=a,S_t=s)=1
$$

Тогда 

$$
    Q(s, a) = \dfrac{\sum\limits_{t\in\mathcal{T}(s, a)}\rho_{t+1:T(t)-1}G_t}{\sum\limits_{t\in\mathcal{T}(s, a)}\rho_{t+1:T(t)-1}}
$$

### Exercise 5.7

In learning curves such as those shown in Figure 5.3 error generally decreases with training, as indeed happened for the ordinary importance-sampling method. But for the weighted importance-sampling method error first increased and then decreased. Why do you think this happened?

![alt text](image-4.png)

Второй вариант более склонен к расчёту функции ценности по сэмплирующей стратегии. А так как она носит более исследовательский характер, она зачастую будет выбирать неоптимальные действия, поэтому ошибка будет сперва расти.


### Exercise 5.8

The results with Example 5.5 and shown in Figure 5.4 used a first-visit MC method. Suppose that instead an every-visit MC method was used on the same problem. Would the variance of the estimator still be infinite? Why or why not?

В формуле для вариации будет больше слагаемых, чем в first-visit методе, так как они все неотрицательны, то да, вариация останется бесконечной.

### Exercise 5.9

Modify the algorithm for first-visit MC policy evaluation (Section 5.1) to use the incremental implementation for sample averages described in Section 2.4.

![alt text](image-5.png)

Нужно изменить последние две строки на:

$$
    N(S_t) \leftarrow N(S_t) + 1 \\
    V(S_t) \leftarrow V(S_t) + \dfrac{1}{N(S_t)} \left[ G - V(S_t) \right]
$$

Инициализируем $N(S_t) = 0$ -- количество посещений состояния $S_t$ среди всех эпизодов.

### Exercise 5.10

Derive the weighted-average update rule (5.8) from (5.7). Follow the pattern of the derivation of the unweighted rule (2.3).

$$
    V_{n+1} = \dfrac{\sum_{k=1}^{n}W_k G_k}{C_n} \\
    V_{n + 1} C_n = \sum_{k=1}^{n}W_k G_k \\
    V_{n + 1} C_n = W_n G_n + \sum_{k=1}^{n-1}W_k G_k \\
    V_{n + 1} C_n = W_n G_n + C_{n - 1} V_{n} \\ 
    V_{n + 1} C_n = W_n G_n + \left( C_n - W_n \right) V_{n} = W_n G_n + C_n V_n - W_n V_n \\
    V_{n + 1} = V_n + \dfrac{W_n}{C_n} \left[ G_n - V_n \right]
$$  

### Exercise 5.11

In the boxed algorithm for off-policy MC control, you may have been 
expecting the W update to have involved the importance-sampling ratio $\dfrac{\pi(A_t|S_t)}{b(A_t|S_t)}$ , but instead it involves $\dfrac{1}{b(A_t|S_t)}$ . Why is this nevertheless correct?

В данном случае такое выражение будет верным, потому что подразумевается, что целевая стратегия будет жадной, поэтому вероятность выбора конкретного действия будет равна 1.