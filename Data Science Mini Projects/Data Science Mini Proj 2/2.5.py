import matplotlib.pyplot as plt

x1 = [1,2,3]
y1 = [2,4,1]
plt.plot(x1, y1, label = 'Line 1')
x2 = [1,2,3]
y2 = [4,1,3]
plt.plot(x2, y2, label = 'Line 2')
x3 = [1,2,3]
y3 = [3,2.5,2]
plt.plot(x3, y3, label = 'Line 3')
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Two lines on same graph')
plt.legend()
plt.show()