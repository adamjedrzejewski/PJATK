import pickle

import tkinter as tk
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from numpy.random import seed
from keras.layers import Dense, Activation, Dropout


model_output_file = "model.sav"
data_file = "dane.csv"

window = tk.Tk()
window.title("SUML TASK 14")
window.minsize(300, 300)

def create_model(X_train, lyrs=[8], act='linear', opt='Adam', dr=0.0):
    seed(42)
    model = Sequential()
    model.add(Dense(lyrs[0], input_dim=X_train.shape[1], activation=act))
    for i in range(1,len(lyrs)):
        model.add(Dense(lyrs[i], activation=act))
    model.add(Dropout(dr))
    model.add(Dense(1, activation='sigmoid'))  
    model.compile(loss='binary_crossentropy', optimizer=opt, metrics=['accuracy'])
    return model

def train_network(df):
    X_train = df[pd.notnull(df['Survived'])].drop(['Survived'], axis=1)
    y_train = df[pd.notnull(df['Survived'])]['Survived']
    X_test = df[pd.isnull(df['Survived'])].drop(['Survived'], axis=1)

    model = create_model(X_train)
    model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.2, verbose=0)
    return model

def save_model(model):
    with open(model_output_file, 'wb') as f:
        pickle.dump(model, f)

def preprocess_data(df):
    df['Sex'] = df['Sex'].astype('category')
    df['Sex'] = df['Sex'].cat.codes
    df['Embarked'] = df['Embarked'].astype('category')
    df['Embarked'] = df['Embarked'].cat.codes

    df.dropna()
    df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)

    scaler = StandardScaler()
    for var in ['Age', 'Fare', 'Parch', 'Pclass', 'SibSp']:
        df[var] = df[var].astype('float64')
        df[var] = scaler.fit_transform(df[var].values.reshape(-1, 1))

    return df

def handle_button_press(event):
    data = pd.read_csv(data_file)
    data = preprocess_data(data)
    print(data.dtypes)
    model = train_network(data)
    save_model(model)

    label = tk.Label(window, text=f"Model have been saved to: {model_output_file}")
    label.pack()


button = tk.Button(text="Train network")
button.bind("<Button-1>", handle_button_press)
button.pack()

# Start the event loop.
window.mainloop()
