# importing the required module
import matplotlib.pyplot as plt
import seaborn as sns
# use to set style of background of plot
sns.set(style ="whitegrid")
# loading data-set
iris = sns.load_dataset('iris');
# plotting strip plot with seaborn
# deciding the attributes of dataset on which plot should be made
ax = sns.swarmplot(x = 'sepal_length', y = 'species', data = iris);
# giving title to the plot
plt.title('Graph')
# function to show plot
plt.show()