import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
#Data from excel sheet "sampledata"
data=pd.read_excel('F:/sampledata.xlsx','Sheet1')
print(data.shape)
print(data.head())
temperature=data['Temperature'].values
coffeesales=data['Coffee Sales'].values
X=np.array([temperature]).T
Y=np.array(coffeesales)
# Regression Model construction :Best fit line
rmodel=LinearRegression()
rmodel=rmodel.fit(X,Y)
# Model Parameters: slope and intercept
slope=rmodel.coef_
intercept=rmodel.intercept_
print('slope : ',slope)
print('intercept :',intercept)
# Model Evaluation
Y_predict=rmodel.predict(X)
rmse=np.sqrt(mean_squared_error(Y,Y_predict))
r2=rmodel.score(X,Y)
print('RMSE',rmse)
print('R-Squared error',r2)
# Model Visualization
plt.scatter(temperature,coffeesales,marker='*',edgecolors='r')
plt.plot(temperature,Y_predict,'-bo')
plt.show()