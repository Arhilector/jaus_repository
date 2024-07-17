import pandas as pd

df = pd.read_csv("World-happiness-report-2024.csv") #чтение файла

print(df.head(3)) #первые 3 строчки
print(df.tail(3)) #последние 3 строчки

print(df.info()) #информация

print(df.describe()) #статистика


print (df[['Country name', 'Regional indicator', 'Ladder score']])
#вывод нужных столбцов

print (df[df['Healthy life expectancy'] > 0.7])

