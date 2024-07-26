from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
import pandas as pd
import matplotlib.pyplot as plt

# Если используем Google Chrome, то пишем driver = webdriver.Chrome()
driver = webdriver.Chrome()

# URL страницы
url = 'https://www.divan.ru/ufa/category/divany-i-kresla'

# Открытие страницы
driver.get(url)

# Ждем некоторое время, чтобы страница полностью загрузилась
time.sleep(5)

# Парсинг цен
prices = driver.find_elements(By.CSS_SELECTOR, 'span.ui-LD-ZU.KIkOH[data-testid="price"]')

# Открытие CSV файла для записи
with open('divan-prieces.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Записываем заголовок столбца

    # Записываем цены в CSV файл
    for price in prices:
        writer.writerow([price.text])

# Закрытие драйвера
driver.quit()

def clean_price(price):
    # Удаляем "руб" и преобразуем в число
    return int(price.replace('руб.', '').replace(' ', ''))

# Чтение данных из исходного CSV файла и их обработка
input_file = 'divan-prieces.csv'
output_file = 'divan-prieces-clean.csv'

with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
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

# Загрузка данных из очищенного CSV файла
data = pd.read_csv(output_file)

# Создание столбца для индексов, так как у нас есть только один столбец "Price"
data['Index'] = range(1, len(data) + 1)

# Расчет средней цены
average_price = data['Price'].mean()
print(f'Средняя цена диванов: {average_price:.2f} руб.')

# Создание диаграммы рассеивания
plt.figure(figsize=(10, 6))
plt.scatter(data['Index'], data['Price'], c='blue', marker='o', label='Цена дивана')
plt.axhline(y=average_price, color='red', linestyle='--', label=f'Средняя цена: {average_price:.2f} руб.')
plt.title('Диаграмма рассеивания цен диванов')
plt.xlabel('Индекс')
plt.ylabel('Цена (руб.)')
plt.legend()

# Отображение графика
plt.grid(True)
plt.show()


