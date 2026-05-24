# Task 3: Feature Engineering
# Create a new boolean column called is_eligible which is True if the student has less than 5 absences
# AND their G3 grade is above 12. Count how many students meet this criteria.
import pandas as pd
df = pd.read_csv("student-mat.csv", sep=';')
df['is_eligible'] = (df['absences'] < 5) & (df['G3'] > 12)
eligible_count = df['is_eligible'].sum()
print("Number of eligible students:", eligible_count)