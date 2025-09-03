import tkinter as tk
from PIL import Image, ImageDraw
import numpy as np
from keras.models import load_model

# Cargar modelo
red = load_model("red.keras")

# Crear ventana
ventana = tk.Tk()
ventana.title("Dibuja un número")

# Canvas
canvas = tk.Canvas(ventana, width=280, height=280, bg='purple')
canvas.pack()

# Etiqueta para mostrar la predicción
pred_label = tk.Label(ventana, text="Predicción: ", font=("Arial", 16))
pred_label.pack(pady=10)

# Imagen interna para guardar el dibujo
imagen = Image.new("L", (28, 28), 0)
dibujar = ImageDraw.Draw(imagen)

def dibujar_con_mouse(event):
    x = event.x
    y = event.y
    r = 6  # radio del pincel
    # Dibuja el círculo en el canvas
    canvas.create_oval(x - r, y - r, x + r, y + r, fill="white", outline="white")
    # Escalar coordenadas a 28x28
    x_i = event.x * 28 // 280
    y_i = event.y * 28 // 280
    dibujar.ellipse([x_i - 1, y_i - 1, x_i + 1, y_i + 1], fill=255)

canvas.bind("<B1-Motion>", dibujar_con_mouse)

# Botón Limpiar
def limpiar_canvas():
    canvas.delete("all")
    dibujar.rectangle([0, 0, 28, 28], fill=0)
    pred_label.config(text="Predicción: ")  # Limpiar predicción

# Predicción
def prediccion():
    imagen_redimensionada = imagen.resize((28, 28))
    img_array = np.array(imagen_redimensionada) / 255.0
    img_array = np.expand_dims(img_array, axis=-1)
    img_array = np.expand_dims(img_array, axis=0)
    
    resultado = red.predict(img_array, verbose=0)
    pred = np.argmax(resultado)
    
    # Mostrar predicción en la etiqueta
    pred_label.config(text=f"Predicción: {pred}")

# Botones
tk.Button(ventana, text="Limpiar", command=limpiar_canvas).pack(side="left", padx=10, pady=10)
tk.Button(ventana, text="Predecir", command=prediccion).pack(side="right", padx=10, pady=10)

ventana.mainloop()
