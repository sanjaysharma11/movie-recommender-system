import pandas as pd
import ast

# Load the dataset
df = pd.read_csv("tmdb_5000_movies.csv")

# Convert 'genres' to category list
def extract_categories(genre_str):
    try:
        genres = ast.literal_eval(genre_str)
        return [genre['name'].lower() for genre in genres]
    except:
        return []

df['category_list'] = df['genres'].apply(extract_categories)

# Main logic
if __name__ == "__main__":
    print("🎬 Category-Based Movie Recommendation 🎬")
    user_input = input("Enter a movie category (e.g., horror, comedy, crime): ").lower().strip()

    # Filter movies by category
    filtered_movies = df[df['category_list'].apply(lambda categories: user_input in categories)]
    filtered_movies = filtered_movies.sort_values(by='popularity', ascending=False).reset_index(drop=True)

    if filtered_movies.empty:
        print(f"\n⚠️ No movies found with category: {user_input}")
    else:
        print(f"\n🎯 Showing results for '{user_input.title()}' category:")

        index = 0
        step = 10

        while index < len(filtered_movies):
            # Show next 10 movies
            end_index = min(index + step, len(filtered_movies))
            for i in range(index, end_index):
                print(f"{i+1}. {filtered_movies.loc[i, 'title']}")

            index += step

            # Ask if user wants more
            if index < len(filtered_movies):
                more = input("\n🔁 See more movies? (yes/no): ").lower().strip()
                if more != 'yes':
                    print("\n✅ Thanks for using the movie recommendation system!")
                    break
            else:
                print("\n✅ End of results.")
