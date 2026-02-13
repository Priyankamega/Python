import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


df = pd.DataFrame({
    'Date': ['2023-01-01', '02-01-2023', 'Invalid'],
    'Category': ['Apple', 'apple', 'Banana'],
    'Value': [10, 1500, 20],
    'Missing': [1, np.nan, 3]
})

print("Original Data:\n", df)


df.drop_duplicates(inplace=True)


df['Missing'] = df['Missing'].fillna(df['Missing'].mean())


df['Date'] = pd.to_datetime(df['Date'], errors='coerce')


df['Date'] = df['Date'].ffill()


df['Category'] = df['Category'].str.lower()


df['Value'] = df['Value'].clip(upper=100)


scaler = MinMaxScaler()
df['Value_norm'] = scaler.fit_transform(df[['Value']])

print("\nCleaned Data:\n", df)
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


data = [12, 15, 14, 10, 18, 20, 22, 15, 17, 19, 16, 14, 13, 15, 18]


plt.figure(figsize=(10, 4))
plt.plot(data, marker='o', linestyle='-', color='b')
plt.title('Line Plot of Data')
plt.xlabel('Index')
plt.ylabel('Value')
plt.grid(True)
plt.show()


plt.figure(figsize=(6, 4))
sns.boxplot(data=data, color='lightgreen')
plt.title('Box Plot of Data')
plt.show()


plt.figure(figsize=(8, 4))
plt.hist(data, bins=5, color='orange', edgecolor='black')
plt.title('Histogram of Data')
plt.xlabel('Value Range')
plt.ylabel('Frequency')
plt.show()

