# Reconocimiento de Números Manuscritos ✍️🔢

Este proyecto implementa un sistema de reconocimiento de dígitos manuscritos mediante una Red Neuronal Convolucional (CNN) entrenada con el dataset MNIST.
El sistema permite al usuario dibujar un número en una interfaz gráfica y obtener en tiempo real la predicción del modelo.

## 🚀 Características principales

✅ Red Neuronal Convolucional (CNN): modelo robusto para la clasificación de dígitos manuscritos.

✅ Entrenamiento con MNIST: dataset estándar que asegura buena precisión y generalización.

✅ Interfaz gráfica interactiva (Tkinter): el usuario puede dibujar un número y recibir la predicción al instante.

✅ Preprocesamiento de imágenes: limpieza y normalización del input antes de la clasificación.

✅ Predicciones en tiempo real: integración directa entre el modelo y la interfaz.

🖼️ Vista previa

(Aquí puedes añadir capturas de pantalla o un GIF mostrando cómo el usuario dibuja y recibe la predicción)

## 🛠️ Tecnologías utilizadas

Python

TensorFlow / Keras

Tkinter

NumPy, Matplotlib (para preprocesamiento y visualización)

## 📂 Estructura del proyecto
├── model/                 # Entrenamiento y almacenamiento del modelo CNN

├── gui/                   # Código de la interfaz gráfica con Tkinter

├── utils/                 # Funciones de preprocesamiento y utilidades

├── main.py                # Punto de entrada de la aplicación

├── requirements.txt       # Dependencias del proyecto

└── README.md              # Documentación del proyecto

## ⚡ Cómo ejecutar el proyecto

Clonar el repositorio:

git clone https://github.com/iratxe-pm/Reconocimiento-Numeros.git
cd Reconocimiento-Numeros


Instalar dependencias:

pip install -r requirements.txt


Ejecutar la aplicación:

python main.py

## 🎯 Resultados

Precisión alcanzada con el dataset MNIST: ~90%

Predicciones inmediatas en la interfaz gráfica.

Experiencia interactiva para el usuario final.

## 📌 Futuras mejoras

 Guardar y cargar predicciones anteriores.

 Añadir soporte para más idiomas en la interfaz.

 Mejorar la interfaz con Tkinter avanzado o PyQt.

## 👩‍💻 Autor

Proyecto desarrollado por Iratxe Parra Moreno
