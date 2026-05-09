import pandas as pd

# Load dataset with correct separator
df = pd.read_csv("student-mat.csv", sep=';')

print(df.columns)

dropouts_df = df[df['G3'] == 0]


print(dropouts_df.head())