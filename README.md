# Reconocimiento de Números Manuscritos ✍️🔢

Este proyecto implementa un sistema de reconocimiento de dígitos manuscritos mediante una Red Neuronal Convolucional (CNN) entrenada con el dataset MNIST.
El sistema permite al usuario dibujar un número en una interfaz gráfica y obtener en tiempo real la predicción del modelo.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)
![Keras](https://img.shields.io/badge/Keras-red)
![Pillow](https://img.shields.io/badge/Pillow-✓-brightgreen)
![NumPy](https://img.shields.io/badge/NumPy-✓-blue)
![pandas](https://img.shields.io/badge/pandas-✓-lightblue)
![License](https://img.shields.io/badge/license-MIT-green)


## 🚀 Características principales

✅ Red Neuronal Convolucional (CNN): modelo robusto para la clasificación de dígitos manuscritos.

✅ Entrenamiento con MNIST: dataset estándar que asegura buena precisión y generalización.

✅ Interfaz gráfica interactiva (Tkinter): el usuario puede dibujar un número y recibir la predicción al instante.

✅ Preprocesamiento de imágenes: limpieza y normalización del input antes de la clasificación.

✅ Predicciones en tiempo real: integración directa entre el modelo y la interfaz.

## 🛠️ Tecnologías utilizadas

Python

TensorFlow / Keras

Tkinter

NumPy, Matplotlib (para preprocesamiento y visualización)

## 📂 Estructura del proyecto
├── red_neuronal.py        # Entrenamiento de la red

├── red_keras              # Almacenamiento de los resultados del entrenamiento de la red

├── main.py                # Punto de entrada de la aplicación

├── requirements.txt       # Dependencias del proyecto

└── README.md              # Documentación del proyecto

## ⚡ Cómo ejecutar el proyecto

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/iratxe-pm/Reconocimiento-Numeros.git
   cd Reconocimiento-Numeros


2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt


3. Ejecutar la aplicación:
   ```bash
   python main.py


## 🎯 Resultados

Precisión alcanzada con el dataset MNIST: ~90%

Predicciones inmediatas en la interfaz gráfica.

Experiencia interactiva para el usuario final.

## 📌 Futuras mejoras

 - Guardar y cargar predicciones anteriores.

 - Añadir soporte para más idiomas en la interfaz.

 - Mejorar la interfaz con Tkinter avanzado o PyQt.

## 👩‍💻 Autor

Proyecto desarrollado por Iratxe Parra Moreno
