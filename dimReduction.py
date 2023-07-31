from matplotlib import pyplot as plt
import numpy as np

class PCA:
    def __init__(self, n_components):
        self.n_components = n_components
        self.components = None
        self.mean = None

    def fit(self, X):
        # need mean
        self.mean = np.mean(X, axis=0)
        # calc auto-covarience with np.cov feats*samples
        cov = np.cov((X - self.mean).T)
        # calc eignvectors and eigenvalues
        eignvals, eignvects = np.linalg.eig(cov)
        ids = np.argsort(eignvals, axis=0)[::-1]
        ids = ids[:self.n_components]
        self.components = eignvects[ids]

    def transform(self, X):
        Xm = X - self.mean
        return np.dot(Xm, self.components.T)

# ==============================================

from sklearn import datasets
iris = datasets.load_iris()
X, y = iris.data, iris.target

pca = PCA(2)
pca.fit(X)
X_projected = pca.transform(X)

print("Shape of X:", X.shape)
print("Shape of transformed X:", X_projected.shape)

x1 = X_projected[:, 0]
x2 = X_projected[:, 1]
# x3 = X_projected[:, 2]

fig1 = plt.figure(1)
plt.scatter(
    x1, x2, c=y, edgecolor="none", alpha=0.8, cmap=plt.cm.get_cmap("viridis", 3)
)

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.colorbar()
plt.show()

# 3D projection
# fig2 = plt.figure(2, figsize=(8, 6))
# ax = fig2.add_subplot(111, projection="3d")

# ax.scatter(x1, x2, x3, c=y, cmap=plt.cm.Set1, edgecolor="k")

# ax.set_title("Iris dataset 3D visualisation")
# ax.set_xlabel("Sepal Length")
# ax.xaxis.set_ticklabels([])
# ax.set_ylabel("Sepal Width")
# ax.yaxis.set_ticklabels([])
# ax.set_zlabel("Petal Length")
# ax.zaxis.set_ticklabels([])

# plt.show()
