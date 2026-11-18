import numpy as np
import random
import matplotlib.pyplot as plt

# Grid environment
ROWS = 4
COLS = 4

START = 0
GOAL = 15
OBSTACLES = [5, 9]

# Actions: Up, Down, Left, Right
ACTIONS = [0, 1, 2, 3]

# Q-table initialization
q_table = np.zeros((ROWS * COLS, len(ACTIONS)))

# Learning parameters
learning_rate = 0.8
discount_factor = 0.95
epsilon = 1.0
epsilon_decay = 0.995
min_epsilon = 0.01
episodes = 2000

# Environment function
def environment(state, action):

    row = state // COLS
    col = state % COLS

    if action == 0:
        row -= 1
    elif action == 1:
        row += 1
    elif action == 2:
        col -= 1
    elif action == 3:
        col += 1

    # Prevent moving outside grid
    row = max(0, min(row, ROWS - 1))
    col = max(0, min(col, COLS - 1))

    new_state = row * COLS + col

    # Goal reward
    if new_state == GOAL:
        return new_state, 100, True

    # Obstacle penalty
    if new_state in OBSTACLES:
        return new_state, -100, True

    return new_state, -1, False


# Training the agent
rewards = []

for episode in range(episodes):

    state = START
    total_reward = 0

    for step in range(100):

        # Epsilon-greedy action selection
        if random.random() < epsilon:
            action = random.choice(ACTIONS)
        else:
            action = np.argmax(q_table[state])

        next_state, reward, done = environment(
            state, action
        )

        # Q-learning update
        old_value = q_table[state, action]

        next_max = np.max(q_table[next_state])

        new_value = old_value + learning_rate * (
            reward + discount_factor * next_max - old_value
        )

        q_table[state, action] = new_value

        state = next_state
        total_reward += reward

        if done:
            break

    rewards.append(total_reward)

    # Reduce exploration
    epsilon = max(
        min_epsilon,
        epsilon * epsilon_decay
    )

# Display training results
print("Training Completed Successfully!")
print("Total Episodes:", episodes)
print("Final Exploration Rate:", round(epsilon, 3))

# Test the trained agent
state = START
path = [state]

for step in range(30):

    action = np.argmax(q_table[state])

    next_state, reward, done = environment(
        state, action
    )

    state = next_state
    path.append(state)

    if done:
        break

# Display learned path
print("\nLearned Path:")

for position in path:
    print("(" + str(position // COLS) +
          ", " + str(position % COLS) + ")")

if path[-1] == GOAL:
    print("\nAgent successfully reached the goal!")
else:
    print("\nAgent did not reach the goal.")

# Visualize the environment
grid = np.zeros((ROWS, COLS))

for obstacle in OBSTACLES:
    grid[obstacle // COLS, obstacle % COLS] = -1

grid[GOAL // COLS, GOAL % COLS] = 2

plt.figure(figsize=(6, 6))
plt.imshow(grid, cmap="coolwarm")

for position in path:
    row = position // COLS
    col = position % COLS
    plt.text(col, row, "A", ha="center",
             va="center", color="black")

plt.title("Reinforcement Learning - Q Learning")
plt.xticks(range(COLS))
plt.yticks(range(ROWS))
plt.grid()
plt.show()

# Training reward graph
plt.figure(figsize=(8, 4))
plt.plot(rewards)
plt.title("Agent Training Rewards")
plt.xlabel("Episodes")
plt.ylabel("Total Reward")
plt.show()
