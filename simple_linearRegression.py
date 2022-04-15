import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
#Data: {temperature & icesales}=>Independent & Dependent Variable
temperature=[20,25,30,35,40]
icesales=[13,21,25,35,38]
X=np.array([temperature]).T
Y=np.array(icesales)
# Regression Model construction :Best fit line
rmodel=LinearRegression()
rmodel=rmodel.fit(X,Y)
# Model Parameters: slope and intercept
rmodel_slope=rmodel.coef_
rmodel_intercept=rmodel.intercept_
print('Model Slope',rmodel_slope)
print('Model Intercept',rmodel_intercept)
# Model Evaluation
Y_predict=rmodel.predict(X)
rmse=np.sqrt(mean_squared_error(Y,Y_predict))
r2=rmodel.score(X,Y)
print('Model RMSE',rmse)
print('R-Squared Error',r2)
# Model Visualization
plt.scatter(temperature,icesales,marker='*',edgecolors='r')
plt.plot(temperature,Y_predict,'-bo')
plt.show()
