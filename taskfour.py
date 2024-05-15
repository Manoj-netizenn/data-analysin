import pandas as pd

import warnings
warnings.filterwarnings('ignore')
# Load the CSV file into a DataFrame
df = pd.read_csv('Dataset .csv')

# Convert 'yes' and 'no' to True and False in the 'online_delivery' column
df['Has Online delivery'] = df['Has Online delivery'].map({'Yes': True, 'no': False})

# Calculate the percentage of restaurants that offer online delivery


percentage_online_delivery = (df['Has Online delivery'].sum() / len(df)) * 100

print(f"Percentage of restaurants that offer online delivery: {percentage_online_delivery:.2f}%")

#df['Aggregate rating'] = df['Aggregate rating'].fillna(0)
df['Has Online delivery'] = df['Has Online delivery'].map({'Yes': True, 'no': False})

avg_rating_with_delivery = df[df['Has Online delivery']=='Yes']['Aggregate rating'].mean()
avg_rating_without_delivery = df[df['Has Online delivery']=='no']['Aggregate rating'].mean()

print(f"Average rating for restaurants with online delivery: {avg_rating_with_delivery:.2f}")
print(f"Average rating for restaurants without online delivery: {avg_rating_without_delivery:.2f}")

    # Compare the average ratings
if avg_rating_with_delivery > avg_rating_without_delivery:
    print("Restaurants with online delivery have higher average rating.")
elif avg_rating_with_delivery < avg_rating_without_delivery:
    print("Restaurants without online delivery have higher average rating.")
else:
    print("Average ratings are the same for both groups.")