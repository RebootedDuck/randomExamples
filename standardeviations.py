import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate a series of random numbers (1000 random numbers between 0 and 100)
random_numbers = np.random.uniform(0, 100, 1000)

# Step 2: Calculate the standard deviation
std_deviation = np.std(random_numbers)
mean = np.mean(random_numbers)

# Step 3: Plot the random numbers and their distribution
plt.figure(figsize=(10, 6))

# Plot histogram to visualize the distribution of the random numbers
plt.hist(random_numbers, bins=30, alpha=0.7, color='blue', edgecolor='black')

# Add mean and standard deviation lines
plt.axvline(mean, color='red', linestyle='dashed', linewidth=2, label=f'Mean = {mean:.2f}')
plt.axvline(mean + std_deviation, color='green', linestyle='dotted', linewidth=2, label=f'Mean + 1 Std Dev = {mean + std_deviation:.2f}')
plt.axvline(mean - std_deviation, color='green', linestyle='dotted', linewidth=2, label=f'Mean - 1 Std Dev = {mean - std_deviation:.2f}')

# Add labels and legend
plt.title('Random Numbers Distribution with Mean and Standard Deviation')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()

# Show plot
plt.show()

# Print the standard deviation for reference
print(f'Standard Deviation: {std_deviation:.2f}')
