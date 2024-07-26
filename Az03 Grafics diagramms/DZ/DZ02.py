import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
num_samples = 100  # Количество образцов
data_x = np.random.rand(num_samples)
data_y = np.random.rand(num_samples)

# Построение диаграммы рассеяния
plt.scatter(data_x, data_y, color='blue', marker='o')

# Добавление заголовка и меток осей
plt.title('Диаграмма рассеяния для двух наборов случайных данных')
plt.xlabel('Значения X')
plt.ylabel('Значения Y')

# Отображение диаграммы
plt.show()