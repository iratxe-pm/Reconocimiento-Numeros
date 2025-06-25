from keras.utils import set_random_seed
import pandas as pd
from tensorflow.keras.datasets import mnist
from keras import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.optimizers import SGD

set_random_seed(394867)

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(-1, 28, 28, 1) / 255.0
x_test = x_test.reshape(-1, 28, 28, 1) / 255.0

# Atributos
print(x_train)
#Objetivos
print( y_train)


# Crear red 
red = Sequential([
    Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)), # 32 filtros de 3*3 q hace la conv / imagen de 28x28 píxeles y 1 canal (b y n)
    MaxPooling2D(pool_size=(2, 2)),    
    
    Conv2D(64, kernel_size=(3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),  

    Conv2D(64, kernel_size=(3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),   

    Flatten(),                  # vector 3D -> vector 1D                         

    Dense(128, activation='relu'),
    Dropout(0.3),

    Dense(64, activation='relu'),
    Dropout(0.2),

    Dense(10, activation='softmax')  # Calcula el número más probable
])



red.summary()

# Compilar 
optimizador = SGD(learning_rate=0.01)
red.compile(
    optimizer=optimizador,
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

#Entrena
red.fit(
    x_train,        # entrenamiento
    y_train,         # objetivo
    batch_size=64,                  # Tamaño del "lote" de entrenamiento
    epochs=25,                     # Número de veces que se recorre todo el dataset
    validation_split=0.1,           # Porcentaje de datos usados para validación
    verbose=1                       # Nivel de detalle de la salida en consola
)

#Evalua
red.evaluate(x_test, y_test)

red.save('red.keras')