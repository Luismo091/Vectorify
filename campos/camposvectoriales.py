import numpy as np
import matplotlib.pyplot as plt

# Definimos la constante de gravitación universal
G = 6.67e-11

# Definimos la masa y el radio de la Tierra
M = 5.97e24
R = 6371e3

# Definimos la velocidad angular de la Tierra
omega = 2 * np.pi / (24 * 3600)

# Definimos el rango de valores para x e y en metros
x = np.linspace(-10e6, 10e6, 20)
y = np.linspace(-10e6, 10e6, 20)

# Creamos una malla de puntos
X, Y = np.meshgrid(x, y)

# Calculamos la distancia al centro de la Tierra
r = np.sqrt(X**2 + Y**2 + R**2)

# Calculamos la intensidad del campo gravitacional
g = G * M / r**2

# Calculamos las componentes del vector campo
gx = -g * X / r
gy = -g * Y / r

# Añadimos la componente tangencial debido a la rotación de la Tierra
gt = omega**2 * R
gy = gy + gt

# Graficamos el campo vectorial
plt.figure()
plt.quiver(X, Y, gx, gy, color='blue')
plt.title('Campo gravitacional de la Tierra con los campos vectoriales')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
