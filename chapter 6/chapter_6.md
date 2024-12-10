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

### Exercise 6.3

From the results shown in the left graph of the random walk example it
appears that the first episode results in a change in only $V(A)$. What does this tell you
about what happened on the first episode? Why was only the estimate for this one state
changed? By exactly how much was it changed?

Так как изменилось только это значение, значит, что эпизод завершился в крайнем левом положении. Награда равна нулю, поэтому значение уменьшилось при $\alpha = 0.1$ и $\gamma = 1$:
$$
    V(A) = V(A) + \alpha (R + V(T) - V(A)) = 0.5 + 0.1 \cdot (0 + 0 - 0.5) = 0.45
$$