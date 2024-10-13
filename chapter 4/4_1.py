import numpy as np

# Define constants
GRID_SIZE = 4
TERMINAL_STATES = [(0, 0), (3, 3)]
REWARD = -1
THRESHOLD = 1e-6

# Initialize the value function
V = np.zeros((GRID_SIZE, GRID_SIZE))

# Define possible actions and their effects
actions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

# Function to check if a state is terminal
def is_terminal(state):
    return state in TERMINAL_STATES

# Policy evaluation function
def policy_evaluation():
    global V
    while True:
        delta = 0
        # Iterate through each state in the grid
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if is_terminal((i, j)):
                    continue
                
                v = V[i, j]  # Store old value for convergence check
                new_value = 0
                
                # Evaluate the expected value for each action
                for action in actions:
                    di, dj = actions[action]
                    next_i = max(0, min(GRID_SIZE - 1, i + di))
                    next_j = max(0, min(GRID_SIZE - 1, j + dj))
                    
                    # If moving out of bounds, stay in the same cell
                    if (next_i == i and next_j == j):
                        reward = REWARD
                    else:
                        reward = REWARD
                    
                    new_value += (1 / len(actions)) * (reward + V[next_i, next_j])
                
                V[i, j] = new_value
                delta = max(delta, abs(v - V[i, j]))
        
        # Check for convergence
        if delta < THRESHOLD:
            break

# Run policy evaluation
policy_evaluation()

# Display the estimated value function
print("Estimated Value Function:")
V = V.round()
print(V)