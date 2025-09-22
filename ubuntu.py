import requests
import os
import hashlib
from urllib.parse import urlparse
from pathlib import Path

SAVE_DIR = Path("Fetched_Images")
MAX_FILE_SIZE_MB = 10  


def safe_filename_from_url(url: str) -> str:
    """Extract a safe filename from a URL or generate one."""
    parsed = urlparse(url)
    filename = os.path.basename(parsed.path)
    if not filename:  
        filename = "image_from_web.jpg"
    return filename


def calculate_file_hash(filepath: Path) -> str:
    """Compute SHA256 hash of a file to detect duplicates."""
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def download_image(url: str) -> None:
    """Download and save an image from a given URL with precautions."""
    try:
        response = requests.get(url, stream=True, timeout=10)
        response.raise_for_status()

        
        content_type = response.headers.get("Content-Type", "")
        if "image" not in content_type.lower():
            print(f"⚠ Skipped (not an image): {url}")
            return

        content_length = response.headers.get("Content-Length")
        if content_length and int(content_length) > MAX_FILE_SIZE_MB * 1024 * 1024:
            print(f"⚠ Skipped (file too large > {MAX_FILE_SIZE_MB}MB): {url}")
            return


        filename = safe_filename_from_url(url)
        save_path = SAVE_DIR / filename

        
        base, ext = os.path.splitext(filename)
        counter = 1
        while save_path.exists():
            
            if calculate_file_hash(save_path) == hashlib.sha256(response.content).hexdigest():
                print(f"✓ Skipped duplicate: {filename}")
                return
            save_path = SAVE_DIR / f"{base}_{counter}{ext}"
            counter += 1

    
        with open(save_path, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        print(f"✓ Successfully fetched: {save_path.name}")
        print(f"  → Saved to {save_path}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching {url}: {e}")


def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    SAVE_DIR.mkdir(exist_ok=True)


    urls = input("Please enter image URLs (comma-separated): ").split(",")

    for url in [u.strip() for u in urls if u.strip()]:
        download_image(url)

    print("\nConnection strengthened. Community enriched.")


if __name__ == "__main__":
    main()
