import csv
import pandas as pd
import matplotlib.pyplot as plt

def clean_price(price):
    # Удаляем "₽/мес." и преобразуем в число
    return int(price.replace(' ₽/мес.', '').replace(' ', ''))


# Чтение данных из исходного CSV файла и их обработка
input_file = 'prices.csv'
output_file = 'cleaned_prices.csv'

with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', newline='',
                                                                  encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Читаем заголовок и записываем его в новый файл
    header = next(reader)
    writer.writerow(header)

    # Обрабатываем и записываем данные строк
    for row in reader:
        clean_row = [clean_price(row[0])]
        writer.writerow(clean_row)

print(f"Обработанные данные сохранены в файл {output_file}")

# Загрузка данных из CSV-файла
file_path = 'cleaned_prices.csv'
data = pd.read_csv(file_path)



# Предположим, что столбец с ценами называется 'price'
prices = data['Price']



# Построение гистограммы
plt.hist(prices, bins=10, edgecolor='black')


# Мы можем изменить количество bin-ов по своему усмотрению



# Добавление заголовка и меток осей
plt.title('Гистограмма цен')
plt.xlabel('Цена')
plt.ylabel('Частота')



# Показать гистограмму
plt.show()