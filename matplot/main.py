import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [2, 3, 4, 5]
y1 =[3, 4, 5, 6]

# label the graph
plt.title('graph')
plt.xlabel('x')
plt.ylabel('y and y1')
plt.legend(['this is y', 'this is y1'])

# make graph
plt.plot(x, y)
plt.plot(x, y1)

# display graph
plt.show()