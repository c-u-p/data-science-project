import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10]
y = [2,4,1,5,2,6,8,7,9,10]

plt.plot(x, y, color = 'red', linestyle = 'dashed', linewidth = 3, marker = 'd', markerfacecolor = 'blue', markersize = 10 )
plt.ylim(1,12)
plt.xlim(1,12)

plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.title('Some cool customizations')
plt.show()