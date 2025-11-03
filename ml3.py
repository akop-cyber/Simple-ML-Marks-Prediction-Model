import numpy as np
from sklearn.linear_model import LinearRegression
#--------------------------------------Feeding Data------------------------------------------------------------
x = np.array([
    [1, 8, 60],   # studied 1 hr, slept 8 hrs, 60% attendance
    [2, 7, 70],
    [3, 6, 75],
    [4, 6, 85],
    [5, 5, 90]
])
y = np.array([35, 50, 65, 80, 95])
#--------------------------------------------Model & Training---------------------------------------------------
model = LinearRegression()
model.fit(x,y)
print("m = ",model.coef_)
print("c = ",model.intercept_)
#--------------------------------------------Prediction----------------------------------------------------------
study = float(input("Enter study hours: "))
sleep = float(input("Enter sleep hours: "))
attend = float(input("Enter attendance%: "))

x_new = np.array([[study,sleep,attend]])
y_pred = model.predict(x_new)
print("The predicted marks would be ",y_pred[0])








