import pandas as pd
import chardet

# Определение кодировки файла
with open("Most Streamed Spotify Songs 2024.csv", 'rb') as f:
    result = chardet.detect(f.read())
    encoding = result['encoding']

# Чтение файла с определенной кодировкой
df = pd.read_csv("Most Streamed Spotify Songs 2024.csv", encoding=encoding)


print(df.head(5)) #первые 5 строк


print(df.info()) #информация

print(df.describe()) #статистика



