import pandas as pd
import matplotlib.pyplot as plt

# Sample data
df = pd.read_csv('Dataset .csv')

# Create a histogram or bar chart to visualize the distribution of price ranges
plt.figure(figsize=(1, 6))
df['Average Cost for two'].value_counts().sort_index().plot(kind='bar', color='skyblue')
plt.xlabel('Price Range')
plt.ylabel('Number of Restaurants')
plt.title('Price Range Distribution Among Restaurants')
plt.xticks(rotation=0)
plt.show()

# Calculate the percentage of restaurants in each price range category
price_range_counts = df['Average Cost for two'].value_counts(normalize=True) * 100

print("Percentage of restaurants in each price range category:")
print(price_range_counts)
