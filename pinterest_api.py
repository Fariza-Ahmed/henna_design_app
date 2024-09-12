import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')

if not ACCESS_TOKEN:
    raise ValueError('Access token is missing. Make sure to set ACCESS_TOKEN in your .env file.')

def fetch_images(preference):
    
    if preference == 'geometric':
        url = 'https://api.pinterest.com/v5/boards/1014506322249448265/pins?board_id=1014506322249448265'
    else:
        url = 'https://api.pinterest.com/v5/boards/1014506322249448269/pins?board_id=1014506322249448269'

    
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}',
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        # Extract image URLs from the response
        largest_image_urls = []

        # Loop through each pin and extract the largest resolution image URL
        for item in data["items"]:
            media = item.get("media", {})
            images = media.get("images", {})

            # Find the largest image by comparing width * height
            largest_image = None
            largest_size = 0
        
            for size_key, image_info in images.items():
                width = image_info.get("width", 0)
                height = image_info.get("height", 0)
                resolution = width * height
            
                # Compare resolutions and store the largest one
                if resolution > largest_size:
                    largest_size = resolution
                    largest_image = image_info.get("url")

            if largest_image:  # Check if we found a valid image URL
                largest_image_urls.append(largest_image)
        
        return largest_image_urls
    except requests.RequestException as e:
        print(f"Error fetching images: {e}")
        print(f"Status Code: {response.status_code}")
        print("Response:", response.json())
        return []
