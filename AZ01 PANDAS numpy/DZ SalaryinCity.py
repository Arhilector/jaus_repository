import pandas as pd
df = pd.read_csv('dz.csv')
print(df)

group = df.groupby('City')["Salary"].mean()

df.to_csv ('salaryincity.csv', index = False)

print(group)