import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('eight.csv')

categories = data['Category'].values
values = data['Value'].values

plt.figure(figsize=(10, 6))
plt.bar(categories, values, color='skyblue')
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar chart representation of data')
plt.tight_layout()

plt.show()