#. x=np.array([range(10),range(10,20)])  y=np.array([range(100, 110)]) 인 데이터로 모델을 구성하고 r2 값 확인해보자

import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score


# 1. 데이터

x=np.array([range(10),range(10,20)])
x=x.T

y=np.array([range(100, 110)])
y=y.T

x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    shuffle=True,
    train_size=0.7,
    random_state=155
)

# 2. 모델 구성

model=Sequential()
model.add(Dense(5,input_dim=2))
model.add(Dense(7))
model.add(Dense(10))
model.add(Dense(7))
model.add(Dense(5))
model.add(Dense(1))

# 3. 컴파일, 훈련

model.compile(loss='mse', optimizer='adam')
model.fit(x_train,y_train, epochs=100, batch_size=1)

# 4. 평가, 예측

loss = model.evaluate(x_test,y_test)
print('loss :', loss)

y_predict= model.predict(x_test)

r2=r2_score(y_test,y_predict)
print('r2 :', r2)


plt.plot(x_train,y_train)
plt.show()