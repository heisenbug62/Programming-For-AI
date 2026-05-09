import pandas as pd

df = pd.read_csv("student-mat.csv", sep=';')
attendance_perf = df[['absences', 'G3']]
newDf = attendance_perf.iloc[::10]

print(newDf)

correlation = attendance_perf['absences'].corr(attendance_perf['G3'])

print(correlation)