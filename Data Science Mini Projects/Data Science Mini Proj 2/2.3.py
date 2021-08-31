import matplotlib.pyplot as plt
import seaborn as sea

sea.set(style = 'whitegrid')
iris = sea.load_dataset('iris')
ax = sea.swarmplot(x = 'species', y = 'sepal_length', data = iris)

plt.title('Graph')
plt.show()