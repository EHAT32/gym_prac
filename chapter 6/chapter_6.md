### Exercise 6.1

If V changes during the episode, then (6.6) only holds approximately; what would the difference be between the two sides? Let $V_t$ denote the array of state values
used at time t in the TD error (6.5) and in the TD update (6.2). Redo the derivation
above to determine the additional amount that must be added to the sum of TD errors
in order to equal the Monte Carlo error. 

$$
    G_t - V_t(S_t) = R_{t+1} + \gamma V_{t+1}(S_{t+1}) - V_t(S_t) = \\
    = R_{t+1} + \gamma V_{t+1}(S_{t+1}) - V_t(S_t) + \gamma V_t(S_{t+1}) - \gamma V_t(S_{t+1}) = \\
    = R_{t+1} + \gamma V_t(S_{t+1}) - V_t(S_t) + \gamma \left( V_{t+1}(S_{t+1}) - V_t(S_{t+1}) \right) = \\
    = \dots = \sum\limits_{k=t}^{T-1}\gamma^{k-t}\delta_k + \sum\limits_{k=t}^{T-1}\gamma^{k-t+1}\left( V_{k+1}(S_{k+1}) - V_k(S_{k+1}) \right)
$$

### Excercise 6.2

This is an exercise to help develop your intuition about why TD methods
are often more ecient than Monte Carlo methods. Consider the driving home example
and how it is addressed by TD and Monte Carlo methods. Can you imagine a scenario
in which a TD update would be better on average than a Monte Carlo update? Give
an example scenario—a description of past experience and a current state—in which
you would expect the TD update to be better. Here’s a hint: Suppose you have lots of
experience driving home from work. Then you move to a new building and a new parking
lot (but you still enter the highway at the same place). Now you are starting to learn
predictions for the new building. Can you see why TD updates are likely to be much
better, at least initially, in this case? Might the same sort of thing happen in the original
scenario?

Основное отличие двух методов заключается в том, что MC алгоритм обучается только после завершения эпизода, в то время как TD алгоритм позволяет обучаться по ходу эпизода

TD метод будет работать хуже в случае нестабильных изменений ситуаций (внезапные остановки из-за грузовиков)

### Exercise 6.3

From the results shown in the left graph of the random walk example it
appears that the first episode results in a change in only $V(A)$. What does this tell you
about what happened on the first episode? Why was only the estimate for this one state
changed? By exactly how much was it changed?

Так как изменилось только это значение, значит, что эпизод завершился в крайнем левом положении. Награда равна нулю, поэтому значение уменьшилось при $\alpha = 0.1$ и $\gamma = 1$:
$$
    V(A) = V(A) + \alpha (R + V(T) - V(A)) = 0.5 + 0.1 \cdot (0 + 0 - 0.5) = 0.45
$$

### Exercise 6.4

The specific results shown in the right graph of the random walk example
are dependent on the value of the step-size parameter $\alpha$. Do you think the conclusions
about which algorithm is better would be affected if a wider range of $\alpha$ values were used?
Is there a different, fixed value of $\alpha$ at which either algorithm would have performed
significantly better than shown? Why or why not?

Независимо от размера $\alpha$ ошибка сходится примерно к одному и тому же значнию, просто с разной скоростью. Нет какого-то определённого значения $\alpha$, при котором алгоритм будет работать лучше всего.

### Exercise 6.5

In the right graph of the random walk example, the RMS error of the
TD method seems to go down and then up again, particularly at high $\alpha$’s. What could
have caused this? Do you think this always occurs, or might it be a function of how the
approximate value function was initialized?

Чем дальше начальные значения от истинных, тем больше будет ошибка и тем быстрее она будет уменьшаться. При достижении минимальной ошибки (самых близких значений к истине) последующее обучение будет вносить погрешность (предсказанное значение будет колебаться около истинного значения). Если параметр $\alpha$ будет достаточно велик, то эти отклонения будут ещё больше

### Exercise 6.6

In Example 6.2 we stated that the true values for the random walk example
are 1/6 , 2/6 , 3/6 , 4/6 , and 5/6 , for states A through E. Describe at least two di↵erent ways that
these could have been computed. Which would you guess we actually used? Why?

Подсчитать значения можно динамическим программирование через итерационный метод (динамическим программированием). Состояний не так уж и много, можно явно решить систему уравнений Бэллмана.

Либо можно подсчитать через Монте-Карло