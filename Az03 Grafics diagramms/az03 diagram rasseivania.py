import matplotlib.pyplot as plt

# Пример данных
x = [1, 8, 3, 4, 3, 6, 11, 8, 9, 10]
y = [8, 3, 1, 7, 15, 13, 17, 19, 23, 29]

# Создаем диаграмму рассеивания
plt.scatter(x, y, color='blue', marker='o')

# Добавляем заголовок и метки осей
plt.title('Диаграмма рассеивания примера данных')
plt.xlabel('X ось')
plt.ylabel('Y ось')

# Показываем сетку
plt.grid(True)

# Отображаем диаграмму
plt.show()