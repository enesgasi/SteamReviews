import requests
import json
import pandas as pd

def get_steam_reviews(api_key, app_id):
    lang = 'all'
    url = f"https://store.steampowered.com/appreviews/{app_id}?json=1&filter=recent&language={lang}&review_type=all&purchase_type=all&num_per_page=1000"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "application/json"
    }
    params = {
        "key": api_key
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    if data.get('success'):
        reviews = [review['review'] for review in data['reviews']]
        return reviews
    else:
        print("Failed to fetch reviews:", data.get('error'))
        return []

def save_reviews_to_excel(reviews, output_file):
    cleaned_reviews = [review.replace('\n', ' ').strip() for review in reviews]
    df = pd.DataFrame({'Review': cleaned_reviews})
    df.to_excel(output_file, index=False)
    print(f"Reviews saved to '{output_file}'")

def save_reviews_to_json(reviews, output_file):
    cleaned_reviews = [review.replace('\n', ' ').strip() for review in reviews]
    reviews_dict = {'reviews': cleaned_reviews}
    with open(output_file, 'w') as f:
        json.dump(reviews_dict, f, indent=4)
    print(f"Reviews saved to '{output_file}'")

with open("your_api_key.txt") as file:
    api_key = file.read().strip()


app_id = '1462040'
reviews = get_steam_reviews(api_key, app_id)

if reviews:
    # Save reviews to Excel
    save_reviews_to_excel(reviews, 'steam_reviews.xlsx')

    # Save reviews to JSON
    save_reviews_to_json(reviews, 'steam_reviews.json')
else:
    print("No reviews found.")
