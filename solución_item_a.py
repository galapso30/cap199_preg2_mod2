
# Transcripción del código solución:
import numpy as np
import matplotlib.pyplot as plt

# 1. Definir la función seno y su derivada
def f(x):
    return np.sin(x)

def df(x):
    return np.cos(x)

# 2. Definir los puntos donde se dibujarán las tangentes y sus características
puntos_tangentes = [0, np.pi/4, np.pi/2, np.pi, 3*np.pi/2]
tangent_colors = ['red', 'green', 'blue', 'purple', 'lightseagreen']
tangent_labels_map = {
    0: 'Tangente en x=0',
    np.pi/4: 'Tangente en x=π/4',
    np.pi/2: 'Tangente en x=π/2',
    np.pi: 'Tangente en x=π',
    3*np.pi/2: 'Tangente en x=3π/2'
}

# 3. Generar un rango de valores para la función seno
x_vals = np.linspace(-0.5, 2 * np.pi + 0.5, 400)
y_vals = f(x_vals)

# 4. Crear la figura y los ejes
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='f(x) = sin(x)', color='black', linewidth=2) # f(x)=sin(x) en negro con mayor grosor

# 5. Dibujar las rectas tangentes
for i, punto_x in enumerate(puntos_tangentes):
    punto_y = f(punto_x)
    pendiente = df(punto_x)

    # Generar un rango más amplio alrededor del punto para dibujar la tangente
    x_tangente = np.linspace(punto_x - 1.0, punto_x + 1.0, 100)
    y_tangente = punto_y + pendiente * (x_tangente - punto_x)

    plt.plot(x_tangente, y_tangente,
             label=tangent_labels_map[punto_x],
             linestyle='-', # Cambiado a línea sólida para 'continuas'
             color=tangent_colors[i],
             alpha=0.7,
             linewidth=2) # Rectas tangentes con mayor grosor
    plt.scatter(punto_x, punto_y, color=tangent_colors[i], zorder=5) # Marcar el punto de tangencia con el color de la tangente

# 6. Configurar el gráfico
plt.title('Rectas tangentes a f(x) = sin(x)', fontweight='bold') # Título en negrita
plt.xlabel('x (radianes)')
plt.ylabel('y = f(x)')
plt.grid(True)
plt.axhline(0, color='gray', linewidth=0.5) # Eje x
plt.axvline(0, color='gray', linewidth=0.5) # Eje y
plt.legend()
plt.ylim(-1.1, 1.6) # Ajustar límites para mejor visualización
plt.xlim(-0.5, 6.5) # Ajustar límites del eje x a la visualización
plt.show()
