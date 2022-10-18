print("Shardul Prabhu")
import matplotlib. pyplot as plt
import pandas as pd
import numpy as np
from sklearn import datasets, linear_model,metrics
from sklearn.model_selection import train_test_split
bostondata = datasets.load_boston(return_X_y=False)
a = bostondata.data
b = bostondata.target
a_train,a_test,b_train,b_test = train_test_split(a,b,
test_size=0.4, random_state=42)
regression = linear_model.LinearRegression()
regression.fit(a_train,b_train)
print("Ceffient of Model:", regression.coef_)
print("Variance of the Model:",regression.score(a_test,b_test))
plt.style.use('fivethirtyeight')
plt.scatter(regression.predict(a_train),regression.predict(a_train)-b_train, color='green',s=10,label='Train_data')
plt.scatter(regression.predict(a_test),regression.predict(a_test)-b_test, color='blue',s=10,label='Test_data')
plt.hlines(y=0,xmin=0,xmax=50,linewidth=2)
plt.legend(loc='upper right')
plt.title('Residual errors')
plt.show()
