import requests
import os
from urllib.parse import urlparse

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    url = input("Please enter the image URL: ").strip()
    os.makedirs("Fetched_Images", exist_ok=True)

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path) or "downloaded_image.jpg"
        filepath = os.path.join("Fetched_Images", filename)

        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}\n")
        print("Connection strengthened. Community enriched.")

    except requests.exceptions.MissingSchema:
        print("✗ Invalid URL. Make sure it starts with http:// or https://")
    except requests.exceptions.HTTPError as e:
        print(f"✗ HTTP Error: {e}")
    except requests.exceptions.ConnectionError:
        print("✗ Connection Error: Could not reach the server")
    except requests.exceptions.Timeout:
        print("✗ Timeout: The request took too long")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")

if __name__ == "__main__":
    main()
