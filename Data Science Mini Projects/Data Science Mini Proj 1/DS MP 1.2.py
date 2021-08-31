import matplotlib.pyplot as plt
import seaborn as sns
import os

data1 = sns.load_dataset('student', data_home = os.path.dirname(os.path.abspath("student")))
ax = sns.stripplot(x = "student", y = "marks", data = data1)
plt.title("my own database")
plt.show()