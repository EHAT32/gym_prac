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