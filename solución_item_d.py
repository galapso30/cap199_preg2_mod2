
import pandas as pd
import matplotlib.pyplot as plt

# Suponiendo que ya has cargado el dataset en la variable 'df'

# Crear la figura y los ejes para los subgráficos
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Boxplot de la variable: age
axes[0].boxplot(df['age'].dropna(), patch_artist=True, boxprops=dict(facecolor='lightblue', color='black'),
                medianprops=dict(color='red', linewidth=2))  # Personaliza la línea de la mediana
axes[0].set_title('Boxplot de la Edad', fontsize=14, fontweight='bold')  # Título con mayor tamaño y negrita
axes[0].set_xlabel('Edad', fontsize=12)  # Etiqueta del eje X
axes[0].set_ylabel('Valor', fontsize=12)  # Etiqueta del eje Y
axes[0].grid(True, which='both', axis='y', color='gray', linestyle='-', linewidth=0.5)  # Líneas divisoras continuas en el eje Y

# Boxplot de la variable: bmi
axes[1].boxplot(df['bmi'].dropna(), patch_artist=True, boxprops=dict(facecolor='lightgreen', color='black'),
                medianprops=dict(color='red', linewidth=2))  # Personaliza la línea de la mediana
axes[1].set_title('Boxplot de BMI', fontsize=14, fontweight='bold')  # Título con mayor tamaño y negrita
axes[1].set_xlabel('BMI', fontsize=12)  # Etiqueta del eje X
axes[1].set_ylabel('Valor', fontsize=12)  # Etiqueta del eje Y
axes[1].grid(True, which='both', axis='y', color='gray', linestyle='-', linewidth=0.5)  # Líneas divisoras continuas en el eje Y

# Boxplot de la variable: cholesterol_level
axes[2].boxplot(df['cholesterol_level'].dropna(), patch_artist=True, boxprops=dict(facecolor='lightcoral', color='black'),
                medianprops=dict(color='red', linewidth=2))  # Personaliza la línea de la mediana
axes[2].set_title('Boxplot de Nivel de Colesterol', fontsize=14, fontweight='bold')  # Título con mayor tamaño y negrita
axes[2].set_xlabel('Colesterol', fontsize=12)  # Etiqueta del eje X
axes[2].set_ylabel('Valor', fontsize=12)  # Etiqueta del eje Y
axes[2].grid(True, which='both', axis='y', color='gray', linestyle='-', linewidth=0.5)  # Líneas divisoras continuas en el eje Y

# Ajustar el diseño para evitar que los subgráficos se sobrepongan
plt.tight_layout()

# Mostrar el gráfico
plt.show()
