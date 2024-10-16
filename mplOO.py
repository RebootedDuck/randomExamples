import matplotlib.pyplot as plt

# Create two figures with different axes
fig1, ax1 = plt.subplots()  # Create first figure and its axes
fig2, ax2 = plt.subplots()  # Create second figure and its axes

# Plot on the first figure
ax1.plot([1, 2, 3], [4, 5, 6])
ax1.set_title('Figure 1')

# Plot on the second figure
ax2.plot([1, 2, 3], [10, 20, 30])
ax2.set_title('Figure 2')

# Display both figures
plt.show()
