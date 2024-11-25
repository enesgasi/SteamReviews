import requests
def get_steam_reviews(api_key, app_id):
    url = f"https://store.steampowered.com/appreviews/{app_id}?json=1&filter=recent&language=all&review_type=all&purchase_type=all&num_per_page=1000"
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

api_key = '733287C02DF0287036428850DA3D4DC3'
app_id = '306130'
reviews = get_steam_reviews(api_key, app_id)
for review in reviews:
    print(review)