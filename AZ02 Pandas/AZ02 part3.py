import pandas as pd
import numpy as np

# Создадим даты с интервалом в один день
dates = pd.date_range(start='2022-07-26', periods=10, freq='D')

# Создадим список из случайных значений
values = np.random.rand(10)

# Создадим датафрейм со словарём
df = pd.DataFrame({'Date': dates, 'Value': values})

# Установим колонку Date в качестве индекса всего датафрейма
df.set_index('Date', inplace=True)

print("Исходный DataFrame:")
print(df)

# Используем ресэмплирование, чтобы установить новый интервал: раз в месяц
month = df.resample('M').mean()

# Посмотрим, как выглядит датафрейм
print("\nDataFrame после ресэмплирования по месяцам:")
print(month)