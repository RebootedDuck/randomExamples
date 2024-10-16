import matplotlib.pyplot as plt
import numpy as np

random_numbers = np.random.uniform(0,100,1000) # Generates set of 1000 numbers of variation 0,100

plt.ion()
fig = plt.figure()
hist = plt.hist(random_numbers)

fig.canvas.mpl_connect('close_event', plt.close(fig))

while True:
    fig.canvas.mpl_connect('close_event', plt.close(fig))
    random_numbers = np.append(arr=random_numbers,values=np.random.uniform(0,max(random_numbers)+100,1000))
    plt.hist(random_numbers)
    plt.draw()
    plt.pause(0.001)