#!/usr/bin/env python3
import sys
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.models import Model
from sklearn.metrics import confusion_matrix
from tensorflow.keras.models import load_model
from sklearn.metrics import ConfusionMatrixDisplay
from tensorflow.keras.layers import Input, Dense, Conv2D, MaxPooling2D, Flatten
from tensorflow.keras.preprocessing.image import ImageDataGenerator

MAX_EPOCHS = 25
INPUT_SHAPE = (100, 100, 3)
TARGET_SIZE = (100, 100)
TRAINING_DIR = './pokemons/train'
TEST_DIR = './pokemons/test'
BATCH_SIZE = 10
CATEGORY_COUNT = 10 # number of classes has been decreased to 10 because with 150 classes training takes long time
MODEL_FILE = './saved_model.h5'
CONFUSSION_MATRIX_FILE = 'confussion_matrix.png'

def build_model():
    in_layer = Input(shape=INPUT_SHAPE)
    conv1 = Conv2D(256, (3, 3), padding='same', activation='relu', name='conv1')(in_layer)
    conv2 = Conv2D(128, (3, 3), padding='same', activation='relu', name='conv2')(conv1)
    pooling1 = MaxPooling2D(pool_size=(2, 2), name='pooling1')(conv2)
    conv3 = Conv2D(128, (3, 3), padding='same', activation='relu', name='conv3')(pooling1)
    conv4 = Conv2D(64, (3, 3), padding='same', activation='relu', name='conv4')(conv3)
    pooling2 = MaxPooling2D(pool_size=(2, 2), name='pooling2')(conv4)
    flatten = Flatten(name='flatten')(pooling2)
    dense1 = Dense(128, activation='relu', name='dense1')(flatten)
    out_layer = Dense(CATEGORY_COUNT, activation='relu', name='dense2')(dense1)
    return Model(inputs=[in_layer], outputs=[out_layer])

def train():
    data_gen= ImageDataGenerator()
    train_gen= data_gen.flow_from_directory(TRAINING_DIR,
                                           shuffle=True,
                                           batch_size=BATCH_SIZE,
                                           target_size=TARGET_SIZE)
    test_gen= data_gen.flow_from_directory(TEST_DIR,
                                           shuffle=True,
                                           batch_size=BATCH_SIZE,
                                           target_size=TARGET_SIZE)
    model = build_model()
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['categorical_accuracy'])
    model.fit(train_gen,
              epochs=MAX_EPOCHS,
              validation_data=test_gen)
    model.save(MODEL_FILE)

def predict():
    gen = ImageDataGenerator().flow_from_directory(TEST_DIR,
                                                   shuffle=True,
                                                   batch_size=BATCH_SIZE,
                                                   target_size=TARGET_SIZE)
    model = load_model(MODEL_FILE)
    y_pred = np.argmax(model.predict(gen), axis=1)
    y_test = gen.classes
    labels = gen.class_indices.keys()
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
    _, ax = plt.subplots(figsize=(10,10))
    disp.plot(cmap=plt.cm.Blues, ax=ax)
    plt.savefig(CONFUSSION_MATRIX_FILE)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("please specify operation: train or predict")
        exit(1)
    if len(sys.argv) > 2:
        print("too many arguments")
        exit(1)
    if len(sys.argv) == 2 and sys.argv[1] == "train":
        train()
        exit(0)
    if len(sys.argv) == 2 and sys.argv[1] == "predict":
        predict()
        exit(0)
    print(f"invalid argument: {sys.argv[1]}")
    exit(1)
