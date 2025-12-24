
import pandas as pd
import matplotlib.pyplot as plt

# Suponiendo que se ha cargado el dataset en la variable 'df'

# Crear la figura y los ejes para los subgráficos
fig, axes = plt.subplots(2, 2, figsize=(20, 12))
fig.suptitle('Cancer', fontsize=16, fontweight='bold')

# 1. Histograma de la columna/variable: age
axes[0, 0].hist(df['age'], bins=5, color='lightblue', edgecolor='black')  # Ajuste en el número de bins
axes[0, 0].set_title('Distribución de la edad')
axes[0, 0].set_xlabel('Edad')
axes[0, 0].set_ylabel('Frecuencia')
axes[0, 0].set_xlim(-1, 110)  # Límite en el eje X de 0 a 100
axes[0, 0].set_ylim(0, 630000)  # Límite en el eje Y de 0 a 650,000

# Agregar líneas divisoras (grillas)
axes[0, 0].grid(True, which='both', axis='both', color='gray', linestyle='-', linewidth=0.5)

# 2. Diagrama de tipo pie de la variable/columna: gender
gender_counts = df['gender'].value_counts()
axes[0, 1].pie(gender_counts,
               labels=gender_counts.index,
               autopct='%1.1f%%',
               colors=['#1f77b4', '#ff7f0e'],  # Colores específicos (azul y naranja)
               startangle=90,  # Asegura que el gráfico comienza en la parte superior
               wedgeprops={'edgecolor': 'black'})  # Borde negro para las secciones
axes[0, 1].set_title('Distribución del genero')

# 3. Distribución de países (columna: country) en un diagrama de barras
country_counts = df['country'].value_counts()
axes[1, 0].bar(country_counts.index, country_counts.values, color='salmon')
axes[1, 0].set_title('Pacientes por país')
axes[1, 0].set_xlabel('País')
axes[1, 0].set_ylabel('Número de pacientes')
axes[1, 0].tick_params(axis='x', rotation=90)  # Rotar las etiquetas del eje x para mejor visibilidad

# 4. Distribución de la etapa del cáncer (columna: cancer_stage) en un diagrama de barras
stage_counts = df['cancer_stage'].value_counts()
axes[1, 1].bar(stage_counts.index, stage_counts.values, color='lightgreen')
axes[1, 1].set_title('Distribución de la etapa del cáncer')
axes[1, 1].set_xlabel('Etapa')
axes[1, 1].set_ylabel('Número de Observaciones')

# Ajustar el diseño
plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Asegurar que el título no se sobreponga
plt.show()
