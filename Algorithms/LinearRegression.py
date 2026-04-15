from sklearn.model_selection import train_test_split
from sklearn.linear_model import  LinearRegression
from sklearn.metrics import mean_absolute_error

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2)

model = LinearRegression()
model.fit(x_train,y_train)
pred = model.predict(x_test)
mae = mean_absolute_error(y_test,pred)