import random
import matplotlib.pyplot as plt


#  https://matplotlib.org/stable/tutorials/colors/colormaps.html   color map for matplotlib
#  tutorial for random walk -->  Eric Matthes - Python Crash Course_ A Hands-On, Project-Based Introduction to Programming-No Starch Press (2019).pdf


x = []
y = []

x_pos = y_pos = 0


def random_walk():
    '''returns x,y co-ord of random walk'''

    global x_pos
    global y_pos
    x_move = random.randrange(-1,2)
    y_move = random.randrange(-1,2)
    x_pos += x_move
    y_pos += y_move
    x.append(x_pos)
    y.append(y_pos)
    return

num_of_walks = 300000
normal_dot_size = 5

for _ in (range(num_of_walks)):
    random_walk()

plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(x, y, c=range(num_of_walks), cmap=plt.cm.YlGnBu, edgecolors='none', s=normal_dot_size)

# Emphasize the first and last points.
ax.scatter(0, 0, c='green', edgecolors='none', s=normal_dot_size*6)
ax.scatter(x[-1], y[-1], c='red', edgecolors='none', s=normal_dot_size*6)

plt.show()

