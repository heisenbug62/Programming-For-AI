import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# Columns:
# InvoiceNo, StockCode, Description, Quantity, InvoiceDate, Price, CustomerID, Country.

df = pd.read_csv('online_retail_II.csv')
# Data Cleaning
df = df.dropna(subset=['Customer ID'])
# Convert InvoiceDate to datetime and handle missing values
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['InvoiceDate'] = df['InvoiceDate'].ffill()
# Separate returns and main sales
returns = df[df['Quantity'] < 0]
main_sales = df[df['Quantity'] >= 0] 

# New column for total spent
df['total_spent'] = df['Quantity']*df['Price']
# New column for month
df['Month'] = df['InvoiceDate'].dt.month
# New column for day of the week
df['DayOfWeek'] = df['InvoiceDate'].dt.dayofweek
# Mapping countries to regions
country_mapping = {
    'United Kingdom': 'UK',
    'Germany': 'Europe',
    'France': 'Europe',
    'Netherlands': 'Europe',
    'Spain': 'Europe',
    'Belgium': 'Europe',
    'Sweden': 'Europe',
    'Norway': 'Europe',
    'Denmark': 'Europe',
    'Italy': 'Europe'
}
df['Region'] = df['Country'].map(country_mapping)

# Top 5 Customers by Total Spent
customer_value = df.groupby('Customer ID')['total_spent'].sum().sort_values(ascending=False).head(5)
print(f"Top 5 Customers by Total Spent:\n{customer_value}")
# Heatmap
heatmap_data = df.pivot_table(values='total_spent', index='DayOfWeek', columns='Month', aggfunc='mean')
print(f"Sales Heatmap Data:\n{heatmap_data}")
# Regional Insights
regional_insights = df.groupby('Region')['Price'].mean()
print(f"Average Unit Price by Region:\n{regional_insights}")

# Outlier Detection using Z-score
df['z_scores'] = stats.zscore(df['Quantity'])
outliers = df[df['z_scores'] > 3]
print(f"Outliers:\n{outliers}")
# Hypothesis Testing
uk_sales = df[df['Region'] == 'UK']['total_spent']
europe_sales = df[df['Region'] == 'Europe']['total_spent']
t_stat, p_value = stats.ttest_ind(uk_sales, europe_sales, equal_var=False)
print(f"T-statistic: {t_stat}, P-value: {p_value}")
print(f"P-value: {p_value}")

if p_value < 0.05:
    print("Reject H0")
    print("There is a statistically significant difference in the average Total_Spent between the UK and Europe.")
else:
    print("Fail to reject H0")
    print("There is no statistically significant difference in the average Total_Spent between the UK and Europe.")

# Plotting of Task 3

customer_value.plot(kind='bar')

plt.title('Top 5 Customers by Total Spent')
plt.xlabel('Customer ID')
plt.ylabel('Total Spent')

plt.show()

plt.figure(figsize=(10, 6))

plt.imshow(heatmap_data, aspect='auto')

plt.colorbar(label='Average Total Spent')

plt.xticks(range(len(heatmap_data.columns)), heatmap_data.columns)
plt.yticks(range(len(heatmap_data.index)), heatmap_data.index)

plt.title('Average Total Spent by Month and Day')
plt.xlabel('Month')
plt.ylabel('Day Of Week')

plt.show()

regional_insights.plot(kind='bar')

plt.title('Average Unit Price by Region')
plt.xlabel('Region')
plt.ylabel('Average Price')

plt.show()

# Plotting of Task 4

plt.hist(df['z_scores'], bins=30)

plt.title('Z-Score Distribution of Quantity')
plt.xlabel('Z-Score')
plt.ylabel('Frequency')

plt.show()

plt.boxplot([uk_sales, europe_sales], labels=['UK', 'Europe'])

plt.title('UK vs Europe Total Spent')
plt.ylabel('Total Spent')

plt.show()