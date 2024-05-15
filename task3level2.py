import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('Dataset .csv')

# Convert 'yes' and 'no' to True and False in the 'online_delivery' column
df['Has Online delivery'] = df['Has Online delivery'].map({'Yes': True, 'no': False})

# Check if the 'rating' column exists
if 'Aggregate rating' in df.columns:
    # Fill NaN values in the 'rating' column with 0
    df['Aggregate rating'] = df['Aggregate rating'].fillna(0.0)

    # Calculate the average ratings for restaurants with and without online delivery
    avg_rating_with_delivery = df[df['Has Online delivery']]['Aggregate rating'].mean()
    avg_rating_without_delivery = df[~df['Has Online delivery']]['Aggregate rating'].mean()

    print(f"Average rating for restaurants with online delivery: {avg_rating_with_delivery:.2f}")
    print(f"Average rating for restaurants without online delivery: {avg_rating_without_delivery:.2f}")

    # Compare the average ratings
    if avg_rating_with_delivery > avg_rating_without_delivery:
        print("Restaurants with online delivery have a higher average rating.")
    elif avg_rating_with_delivery < avg_rating_without_delivery:
        print("Restaurants without online delivery have a higher average rating.")
    else:
        print("Average ratings are the same for both groups.")
else:
    print("The 'rating' column does not exist in the DataFrame.")
