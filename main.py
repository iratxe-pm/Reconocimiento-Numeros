import tkinter as tk
from PIL import Image, ImageDraw
import numpy as np
from keras.models import load_model


red = load_model("red.keras")

# Crear ventana en python
ventana = tk.Tk()
ventana.title("Dibuja un número")

# Canvas
canvas = tk.Canvas(ventana, width=280, height=280, bg='purple')
canvas.pack()

# Imagen interna para guardar el dibujo
imagen = Image.new("L", (28, 28), 0)
dibujar = ImageDraw.Draw(imagen)

def dibujar_con_mouse(event):
    x = event.x
    y = event.y
    r = 6 #radio del pincel
    #crea un cículo con el centro en la coordenada donde está el puntero
    canvas.create_oval(x - r, 
                       y - r, 
                       x + r, 
                       y + r, 
                       fill="white", outline="white")
    # Escalar coordenadas a 28x28 (tamaño de imagen con la que trabaja la red)
    x_i = event.x * 28 // 280
    y_i = event.y * 28 // 280
    dibujar.ellipse([x_i - 1, y_i - 1, x_i + 1, y_i + 1], fill=255)

#se llama a dibujar cada vez q se mantiene presionado el boton izq del mouse
canvas.bind("<B1-Motion>", dibujar_con_mouse)

# Botón Limpiar
def limpiar_canvas():
    canvas.delete("all")
    dibujar.rectangle([0, 0, 28, 28], fill=0)

#prediccion de la red
def prediccion():
    #normalizar la img
    imagen_redimensionada = imagen.resize((28, 28)) 
    img_array = np.array(imagen_redimensionada) / 255.0

    img_array = np.expand_dims(img_array, axis=-1)
    img_array = np.expand_dims(img_array, axis=0)

    resultado = red.predict(img_array, verbose=0)
    pred = np.argmax(resultado)

    print("Predicción:", pred)

tk.Button(ventana, text="Limpiar", command=limpiar_canvas).pack()
tk.Button(ventana, text="Predecir", command=prediccion).pack()


ventana.mainloop()
