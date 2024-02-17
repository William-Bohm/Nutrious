import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

# Get API key and app ID from environment variables
NUTRITION_API_KEY = os.getenv('NUTRITION_API_KEY')
NUTRITION_API_ID = os.getenv('NUTRITION_API_ID')


def get_nutrition_info(query):
    """Send a POST request to Nutritionix API to get nutrition information for a query."""
    url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'
    headers = {
        'Content-Type': 'application/json',
        'x-app-id': NUTRITION_API_ID,
        'x-app-key': NUTRITION_API_KEY
    }
    body = {
        'query': query
    }

    response = requests.post(url, json=body, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return response.text


# Example usage
if __name__ == "__main__":
    query = "grape"
    result = get_nutrition_info(query)
    print(result)
