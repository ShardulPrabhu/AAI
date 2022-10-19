from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

cancer = load_breast_cancer()
cancer.target
sc = StandardScaler()
x_sc = sc.fit_transform(cancer.data)
pca = PCA(n_components=2)
pca.fit(x_sc)
x_pca = pca.transform(x_sc)
print("Original shape: {}".format(str(x_sc.shape)))
print("Reduced shape: {}".format(str(x_pca.shape)))
ax = plt.figure(figsize=(12, 8))
sns.scatterplot(x=x_pca[:, 0], y=x_pca[:, 1], hue=cancer.target, palette='Set1')
plt.legend(cancer.target_names, loc='best')
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.show()
