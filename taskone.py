from collections import Counter
import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('Dataset .csv')

# Calculate the frequency of each cuisine
cuisine_counts = Counter(df['Cuisines'])

# Determine the top three most common cuisines
top_cuisines = cuisine_counts.most_common(3)

# Calculate the total number of restaurants
total_restaurants = len(df)

# Calculate the percentage of restaurants that serve each of the top cuisines
percentage_per_cuisine = [(cuisine, count / total_restaurants * 100) for cuisine, count in top_cuisines]

print("Top three most common cuisines:")
for cuisine, count in top_cuisines:
    print(f"{cuisine}: {count} restaurants")

print("\nPercentage of restaurants that serve each of the top cuisines:")
for cuisine, percentage in percentage_per_cuisine:
    print(f"{cuisine}: {percentage:.2f}%")
