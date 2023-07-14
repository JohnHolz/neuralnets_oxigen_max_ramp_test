import tensorflor as tf

input_shape=(360, 360, 1)

model = tf.keras.Sequential()
model.add(tf.keras.layers.Rescaling(1./255, input_shape=input_shape))
model.add(tf.keras.layers.AveragePooling2D())
model.add(tf.keras.layers.Conv2D(16, (5,5), activation='relu'))
model.add(tf.keras.layers.MaxPooling2D())
model.add(tf.keras.layers.Conv2D(8, (3,3), activation='relu'))
#####
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(8, activation='relu'))
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
#model.compile(loss=MSE, optimizer=rms, metrics=['accuracy'])

model.compile(loss=BC, optimizer=adam, metrics=['accuracy'])





#ramca1

input_shape=(360, 360, 1)

model = tf.keras.Sequential()
model.add(tf.keras.layers.Rescaling(1./255, input_shape=input_shape))
model.add(tf.keras.layers.AveragePooling2D())
model.add(tf.keras.layers.Conv2D(16, (4,4), activation='relu'))
model.add(tf.keras.layers.MaxPooling2D())
model.add(tf.keras.layers.Conv2D(8, (2,2), activation='relu'))
model.add(tf.keras.layers.AveragePooling2D())
#####
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(8, activation='relu'))
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
#model.compile(loss=MSE, optimizer=rms, metrics=['accuracy'])

model.compile(loss=BC, optimizer=adam, metrics=['accuracy'])



#ramca2
input_shape=(360, 360, 1)

def get_compiled_model():
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Rescaling(1./255, input_shape=input_shape))
    model.add(tf.keras.layers.AveragePooling2D())
    model.add(tf.keras.layers.Conv2D(16, (2,2), activation='relu'))
    model.add(tf.keras.layers.MaxPooling2D())
    model.add(tf.keras.layers.Conv2D(8, (2,2), activation='relu'))
    model.add(tf.keras.layers.AveragePooling2D())
    #####
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(8, activation='relu'))
    model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
    #model.compile(loss=MSE, optimizer=rms, metrics=['accuracy'])

    model.compile(loss=BC, optimizer=adam, metrics=['accuracy'])
    return model