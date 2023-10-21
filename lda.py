from matplotlib import pyplot as plt
import numpy as np
from sklearn import datasets
iris = datasets.load_iris()
X, y = iris.data, iris.target

class LDA:

    def __init__(self, n_components):
        self.n_components = n_components
        self.discriminants = None

    def fit(self, X, y):
        n_features = X.shape[1]
        class_labels = np.unique(y)
        mean_overall = np.mean(X, axis=0)

        # calc S_Within: S_W = sum_over_classes((x-mean)*(x-mean)) 
        # S_B = sum_over_classes( n_c * (mean_X_c - mean_overall)^2 )
        S_W = np.zeros((n_features, n_features))
        S_B = np.zeros((n_features, n_features))
        for c in class_labels:
            Xc = X[y==c]
            mean_c = np.mean(Xc, axis=0)
            S_W += (Xc-mean_c).T.dot(Xc-mean_c)
            n_c = Xc.shape[0]
            S_B += n_c*(mean_c-mean_overall).T.dot(mean_c-mean_overall)
        
        A = np.linalg.inv(S_W).dot(S_B)
        eigvals, eigvects = np.linalg.eig(A)
        ids = np.argsort(eigvals, axis=0)[::-1]
        ids = ids[:self.n_components]
        self.discriminants = eigvects[0 : self.n_components]
        
    def transform(self, X):
        # project data on linear discriminants
        return np.dot(X, self.discriminants.T)
    
# ===============================================================

lda = LDA(2)
X12 = np.vstack((X[y == 1], X[y == 2]))
y12 = np.hstack((y[y == 1], y[y == 2]))
lda.fit(X12, y12)
X_t = lda.transform(X12)

x1, x2 = X_t[:,0], X_t[:, 1]
fig1 = plt.figure(1)
plt.scatter(x1, x2, c=y12)

plt.xlabel("Linear disciminant component 1")
plt.ylabel("Linear disciminant component 2")
plt.show()