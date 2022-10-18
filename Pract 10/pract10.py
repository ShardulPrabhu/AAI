print("Shardul Prabhu ")
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
datasrc = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
colnames = ["sepal-length", "sepal-width", "petal-length","petal-width", "Class"]
DS = pd.read_csv(datasrc,names=colnames)
P = DS.drop("Class",axis=1)
Q = DS["Class"]
p_tr,p_ts,q_tr,q_ts = train_test_split(P,Q,test_size=0.2)
#polynomial
cls = SVC(kernel="poly", degree=8)
cls.fit(p_tr,q_tr)
q_pred = cls.predict(p_ts)
print(confusion_matrix(q_ts,q_pred))
print(classification_report(q_ts,q_pred))
#gaussion
cls = SVC(kernel="rbf", degree=8)
cls.fit(p_tr,q_tr)
q_pred = cls.predict(p_ts)
print(confusion_matrix(q_ts,q_pred))
print(classification_report(q_ts,q_pred))
#polynomial
cls = SVC(kernel="poly", degree=8)
cls.fit(p_tr,q_tr)
q_pred = cls.predict(p_ts)
print(confusion_matrix(q_ts,q_pred))
print(classification_report(q_ts,q_pred))
