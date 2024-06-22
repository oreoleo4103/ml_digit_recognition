import os
import time
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import numpy as np
import util
import tensorflow as tf

import keras
from keras import *
from keras import layers
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, InputLayer
from tensorflow.keras.utils import to_categorical



training_data_path = "CompleteDataSet_training_tuples.npy"


print("Loading data...")
training_data = np.load(training_data_path, allow_pickle=True)
print(f"Data loaded")

training_images = util.threeDimToFloat(training_data[:, 0])

training_images = tf.convert_to_tensor(training_images, dtype=tf.float32)
training_labels = training_data[:, 1]

print(f"Labels before conversion:\n{training_labels}")

training_labels = util.convertLabels(training_labels)

print(f"We have {len(training_labels)} for our disposal")
print(f"first two labels (type {type(training_labels)}):\n{training_labels[0]}\n{training_labels[1]}")


tf_labels = tf.convert_to_tensor(training_labels, dtype=tf.float32)


print(f"{training_images[0]}")

print(f"Labels type: {type(training_labels)}")
print(f"Images type: {type(training_images)}")



print(f"Defining model...")

model = keras.Sequential()
model.add(keras.Input(shape=(28, 28, 1)))   # 28x28 B&W images
model.add(layers.Flatten())
model.add(layers.Dense(16, activation="sigmoid"))
model.add(layers.Dense(16, activation="sigmoid"))

model.add(layers.Dense(16, activation="softmax"))



# Compile the model
#print(f"Compiling model...")
model.compile(optimizer=Adam(learning_rate=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])

# Summary of the model
model.summary()

model.fit(training_images, tf_labels, epochs=400, batch_size=500)

model.save("tfmodel.keras")


