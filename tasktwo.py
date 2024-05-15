import pandas as pd

# Assuming you have a pandas DataFrame 'df' with columns 'city', 'restaurant_id', and 'rating'
# Sample data
df = pd.read_csv('Dataset .csv')
# Identify the city with the highest number of restaurants
city_with_most_restaurants = df['City'].value_counts().idxmax()

# Calculate the average rating for restaurants in each city
average_rating_per_city = df.groupby('City')['Aggregate rating'].mean()

# Determine the city with the highest average rating
city_with_highest_avg_rating = average_rating_per_city.idxmax()

print(f"City with the highest number of restaurants: {city_with_most_restaurants}")

print("\nAverage rating for restaurants in each city:")
print(average_rating_per_city)

print(f"\nCity with the highest average rating: {city_with_highest_avg_rating}")
