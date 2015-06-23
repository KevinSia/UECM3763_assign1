import numpy as np
import matplotlib.pyplot as plt

#the integer starting value is now 1200535
np.random.seed(1200535) 

n = 100
x = np.random.random(n)
y = np.random.random(n)
c = np.random.random(n)  # color of points
s = 500 * np.random.random(n)  # size of points

fig, ax = plt.subplots()
im = ax.scatter(x, y, c=c, s=s, cmap=plt.cm.jet)

# Add a colorbar
fig.colorbar(im, ax=ax)

# save the figure
plt.savefig('plot_rnd.png')
plt.show()

# I have my own scatter plot now!