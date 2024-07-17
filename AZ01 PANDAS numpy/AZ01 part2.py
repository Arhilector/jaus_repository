import pandas as pd

df = pd.read_csv("hh.csv")



df['test'] =[new for new in range(29)] #добавление столбца

print(df)

df.drop ('test', axis = 1, inplace = True) #удаление столбца

print(df)


