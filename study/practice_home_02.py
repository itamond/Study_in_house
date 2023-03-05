# load_diabetes 를 이용한 코드 짜보기

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes

#1. 데이터

datasets= load_diabetes()

x= datasets.data
y= datasets.target


"""
  :Attribute Information:
      - age     age in years
      - sex
      - bmi     body mass index
      - bp      average blood pressure
      - s1      tc, total serum cholesterol
      - s2      ldl, low-density lipoproteins
      - s3      hdl, high-density lipoproteins
      - s4      tch, total cholesterol / HDL
      - s5      ltg, possibly log of serum triglycerides level
      - s6      glu, blood sugar level
      """


x_train, x_test, y_train, y_test = train_test_split(x, y,
    train_size=0.9,
    random_state= 72,
    shuffle=True
)


#2. 모델 구성

model=Sequential()
model.add(Dense(10, input_dim=10))
model.add(Dense(100))
model.add(Dense(200))
model.add(Dense(100))
model.add(Dense(10))
model.add(Dense(1))

#3. 컴파일, 훈련

model.compile(loss='mse', optimizer='adam')
model.fit(
    x_train,y_train,
    epochs=100,
    batch_size=5
    )

#4. 평가, 예측

loss= model.evaluate(x_test, y_test)
print("loss :", loss)

y_predict= model.predict(x_test)
r2=r2_score(y_test, y_predict)
print("r2 :", r2)


#r2 : 0.6601526989837079
#r2 : 0.6622384708649621
#r2 : 0.664550072711747