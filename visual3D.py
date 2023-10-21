from sklearn import datasets
from matplotlib import pyplot as plt
iris = datasets.load_iris()
X, y = iris.data, iris.target
plt.figure(0)
ax = plt.subplot(111, projection='3d')
ax.scatter(X[:,0], X[:,1], X[:,2], s=(X[:,3]+1.5)*2, c=y)
plt.show()