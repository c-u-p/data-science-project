import matplotlib.pyplot as plt

x1 = [1,2,3,4,5]
y1 = [2,8,3,10,5]

plt.plot(x1, y1, color = 'red', linewidth = 3)
x2 = [1,2,3,4,5]
y2 = [4,5,3,1,2]


plt.plot(x2, y2, color = 'blue', linewidth = 3)

plt.ylim(1,12)
plt.xlim(1,6)

plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.title('Cricket Teams Scores')
plt.show()