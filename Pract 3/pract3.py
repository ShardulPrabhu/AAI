from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

print("Shardul Prabhu")
data = load_breast_cancer()
print(data.keys())
targets_name = data['target_names']
target_value = data['target']
features_name = data['feature_names']
features = data['data']
print(targets_name[:10])
print(target_value[:10])
print(features_name[:10])
print(features[:10])
X_train, X_test, y_train, y_test = train_test_split(features, target_value, test_size=0.30,random_state=42)
gnb = GaussianNB()
model = gnb.fit(X_train,y_train)
preds = gnb.predict(X_test)
print(preds)
print(accuracy_score(y_test, preds))
