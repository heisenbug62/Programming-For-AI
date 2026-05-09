import pandas as pd

df = pd.read_csv("student-mat.csv", sep=';')

new_df = df[(df['school'] == 'GP') & (df['G3'] >= 10)]
print(new_df.head(10))