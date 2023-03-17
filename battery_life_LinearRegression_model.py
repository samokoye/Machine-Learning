'''
Fred is a very predictable man. For instance, when he uses his laptop, all he does is watch TV shows. He keeps on watching TV shows until 
his battery dies. Also, he is a very meticulous man, i.e. he pays great attention to minute details. He has been keeping logs of every time 
he charged his laptop, which includes how long he charged his laptop for and after that how long was he able to watch the TV. 
Now, Fred wants to use this log to predict how long will he be able to watch TV for when he starts so that he can plan his activities after 
watching his TV shows accordingly.

Challenge

You are given access to Fred’s laptop charging log by reading from the file “trainingdata.txt”. The training data file will consist of 100 lines, 
each with 2 comma-separated numbers.

1. The first number denotes the amount of time the laptop was charged.
2. The second number denotes the amount of time the battery lasted.

The training data file can be downloaded here (this will be the same training data used when your program is run). 
The input for each of the test cases will consist of exactly 1 number rounded to 2 decimal places. For each input, output 1 number: the amount of time 
you predict his battery will last.

Sample Input

1.50

Sample Output

3.00

Scoring

Your score will be 10-X, where X is the sum of the distances you are from expected answer of each test case. 
For instance if there are 2 test cases with expected answer 4 and you print 3 for the first one and 6 for the second one your score will be 10-(1+2) = 7.
'''

#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def batlife(timeCharged):
    # read training data from file
    data = pd.read_csv('trainingdata.txt', delimiter=',', header=None, names=["X", "Y"])
    #print(data)
    data= data[data['X']<4]
    from sklearn.model_selection import train_test_split

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data['X'], data['Y'], test_size=0.2, random_state=42)
    X_train = X_train.values.reshape(-1,1)
    y_train = y_train.values.reshape(-1,1)
    model = LinearRegression()
    model.fit(X_train, y_train)

    # read input from user
    #input_time = float(input("Enter charging time: "))

    # use model to predict battery life for input time
    
    if(timeCharged<4.0):
        predicted_life = model.predict(timeCharged)[0][0]
    else:
        predicted_life = 8.0
    #output and round to 2 decimal place
    print(np.round(predicted_life, 2))

if __name__ == '__main__':
    # read input from user
    timeCharged = np.array(float(input().strip())).reshape(-1,1)
    #call the function batlife to run the LinearRegression model
    batlife(timeCharged)
