import matplotlib.pyplot as plt
import numpy as np

# fix the random state for reproducibility
np.random.seed(100)
np_hist = np.random.normal(loc=0, scale=1, size=1000)
print(np_hist[:10])
# Let's verify the mean and standard deviation of the above distribution.
print(np_hist.mean(),np_hist.std())
# Next, you will use numpy's histogram function, which will return hist and bin_edges.
hist,bin_edges = np.histogram(np_hist)
print(hist)
print(type(hist))
print(bin_edges)


import matplotlib.pyplot as plt
# %matplotlib inline
plt.figure(figsize=[10,8])

plt.bar(bin_edges[:-1], hist, width = 0.5, color='#0504aa',alpha=0.7) # a[:-1]    # # everything except the last item
plt.xlim(min(bin_edges), max(bin_edges))
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Value',fontsize=15)
plt.ylabel('Frequency',fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.ylabel('Frequency',fontsize=15)
plt.title('Normal Distribution Histogram',fontsize=15)
plt.show()

plt.hist()