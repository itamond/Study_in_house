#사이킷런의 트레인 테스트 스플릿을 통해 나눈 
#데이터를 이용한 모델을 구성하고 시각화 해보기

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

#1. 데이터 

x = np.array(range(100))
y = np.array(range(100,200))

x_train, x_test, y_train, y_test = train_test_split(
    x,y,
    train_size=0.8,
    random_state=322,
    shuffle=True
)

#2. 모델구성
model=Sequential()
model.add(Dense(3, input_dim=1))
model.add(Dense(5))
model.add(Dense(3))
model.add(Dense(1))

#3. 컴파일, 훈련
model.compile(loss='mse', optimizer='adam')
model.fit(x_train, y_train,
          epochs=100,
          batch_size=1)

#4. 평가, 예측
loss=model.evaluate(x_test,y_test)
print('loss :', loss)

y_predict=model.predict(x_test)
r2=r2_score(y_test, y_predict)
print('r2 :', r2)

plt.plot(x,y)
plt.scatter(x_train,y_train, color='red')
plt.scatter(x_test,y_test,color='blue')
plt.show()
