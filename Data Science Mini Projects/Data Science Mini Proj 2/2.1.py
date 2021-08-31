import matplotlib.pyplot as plt
import seaborn as zyx

x = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu','Fri','Sat']
y = [5, 6.7, 4, 6, 2, 4.9, 1.8]

ax = zyx.stripplot(x, y)

ax.set(xlabel = 'Days-mondaytofri', ylabel = 'Amount_spent')
plt.title('My first graph')
plt.show()