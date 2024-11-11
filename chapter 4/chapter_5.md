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