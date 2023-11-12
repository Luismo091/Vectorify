import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import math

def sumar_vectores():
    try:
        vector1 = [float(v1x.get()), float(v1y.get())]
        vector2 = [float(v2x.get()), float(v2y.get())]

        resultado = [vector1[0] + vector2[0], vector1[1] + vector2[1]]
        resultado_label.config(text=f"Resultado (Suma): {resultado}")

        # Graficar los vectores
        plt.figure()
        plt.quiver(0, 0, vector1[0], vector1[1], angles='xy', scale_units='xy', scale=1, color='b', label='Vector 1')
        plt.quiver(0, 0, vector2[0], vector2[1], angles='xy', scale_units='xy', scale=1, color='g', label='Vector 2')
        plt.quiver(0, 0, resultado[0], resultado[1], angles='xy', scale_units='xy', scale=1, color='r', label='Resultado')
        plt.xlim(-10, 10)
        plt.ylim(-10, 10)
        plt.legend()
        plt.grid()
        plt.show()
    except ValueError:
        resultado_label.config(text="Ingrese valores válidos")

def restar_vectores():
    try:
        vector1 = [float(v1x.get()), float(v1y.get())]
        vector2 = [float(v2x.get()), float(v2y.get())]

        resultado = [vector1[0] - vector2[0], vector1[1] - vector2[1]]
        resultado_label.config(text=f"Resultado (Resta): {resultado}")

        # Graficar los vectores
        plt.figure()
        plt.quiver(0, 0, vector1[0], vector1[1], angles='xy', scale_units='xy', scale=1, color='b', label='Vector 1')
        plt.quiver(0, 0, vector2[0], vector2[1], angles='xy', scale_units='xy', scale=1, color='g', label='Vector 2')
        plt.quiver(0, 0, resultado[0], resultado[1], angles='xy', scale_units='xy', scale=1, color='r', label='Resultado')
        plt.xlim(-10, 10)
        plt.ylim(-10, 10)
        plt.legend()
        plt.grid()
        plt.show()
    except ValueError:
        resultado_label.config(text="Ingrese valores válidos")

def calcular_magnitud(vector):
    return math.sqrt(vector[0] ** 2 + vector[1] ** 2)

def magnitud_vector():
    try:
        vector = [float(v1x.get()), float(v1y.get())]
        magnitud = calcular_magnitud(vector)
        resultado_label.config(text=f"Magnitud (Vector 1): {magnitud}")
    except ValueError:
        resultado_label.config(text="Ingrese valores válidos")

def multiplicar_por_escalar():
    try:
        vector = [float(v1x.get()), float(v1y.get())]
        escalar = float(escalar_entry.get())
        resultado = [vector[0] * escalar, vector[1] * escalar]
        resultado_label.config(text=f"Resultado (Multiplicación por escalar): {resultado}")

        # Graficar el vector original y el vector escalado
        plt.figure()
        plt.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color='b', label='Vector Original')
        plt.quiver(0, 0, resultado[0], resultado[1], angles='xy', scale_units='xy', scale=1, color='r', label='Resultado')
        plt.xlim(-10, 10)
        plt.ylim(-10, 10)
        plt.legend()
        plt.grid()
        plt.show()
    except ValueError:
        resultado_label.config(text="Ingrese valores válidos")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Vectores")

# Crear etiquetas y campos de entrada para los vectores
v1_label = tk.Label(root, text="Vector 1:")
v1_label.grid(row=0, column=0)
v1x = tk.Entry(root)
v1x.grid(row=0, column=1)
v1y = tk.Entry(root)
v1y.grid(row=0, column=2)

v2_label = tk.Label(root, text="Vector 2:")
v2_label.grid(row=1, column=0)
v2x = tk.Entry(root)
v2x.grid(row=1, column=1)
v2y = tk.Entry(root)
v2y.grid(row=1, column=2)

# Botón para realizar la suma de vectores
sumar_button = tk.Button(root, text="Sumar", command=sumar_vectores)
sumar_button.grid(row=2, column=0)

# Botón para realizar la resta de vectores
restar_button = tk.Button(root, text="Restar", command=restar_vectores)
restar_button.grid(row=2, column=1)

# Etiqueta para mostrar el resultado de suma o resta
resultado_label = tk.Label(root, text="")
resultado_label.grid(row=3, column=1)

# Botón para calcular la magnitud de un vector
magnitud_button = tk.Button(root, text="Calcular Magnitud", command=magnitud_vector)
magnitud_button.grid(row=4, column=1)

# Botón para multiplicar un vector por un escalar
escalar_label = tk.Label(root, text="Escalar:")
escalar_label.grid(row=5, column=0)
escalar_entry = tk.Entry(root)
escalar_entry.grid(row=5, column=1)
multiplicar_button = tk.Button(root, text="Multiplicar por Escalar", command=multiplicar_por_escalar)
multiplicar_button.grid(row=5, column=2)

root.mainloop()
