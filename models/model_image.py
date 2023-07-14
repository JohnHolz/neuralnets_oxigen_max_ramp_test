import tensorflow as tf

## optimizer
rms='rmsprop'
adam='adam'

## loss
SPC = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
CC = tf.keras.losses.CategoricalCrossentropy()
BC = 'binary_crossentropy'
MSE = 'mse'
SCC = 'sparse_categorical_crossentropy'

## last layer
softmax = 'softmax'
sigmoid = 'sigmoid'


model = tf.keras.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
model.add(tf.keras.layers.LSTM(16, activation='relu',return_sequeces =True))
model.add(tf.keras.layers.Dropout(0.3))
model.add(tf.keras.layers.LSTM(10, activation='relu'))
model.add(tf.keras.layers.Dropout(0.3))
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
model.compile(loss=BC, optimizer=adam, metrics=[tf.keras.metrics.Precision(),'accuracy'])

model.fit()


fashion_mnist = tf.keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
train_images.shape
