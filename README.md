# Ubuntu Image Fetcher

**"I am because we are."**

A simple Python script inspired by the Ubuntu philosophy.  
It respectfully fetches an image from the web, saves it locally,  
and organizes it in a folder for later sharing.

---

## ✨ Features
- 🖼️ Fetch multiple images at once (comma-separated URLs).
- 📂 Saves images into a `Fetched_Images/` directory.
- 🔒 Precautions against unsafe downloads:
  - Only saves valid images (`Content-Type: image/*`).
  - Rejects files larger than 10MB.
- 🛡️ Prevents duplicates using SHA256 file hashing.
- ✅ Handles network errors gracefully with clear messages.

---

## Usage
1. Clone this repository  
   ```bash
   git clone https://github.com/Lidiya-Bokona/Ubuntu_Requests.git
   cd Ubuntu_Requests
2. Run the script
    ```bash
    python ubuntu.py
3. Enter an image URL when prompted.
Example:
   Welcome to the Ubuntu Image Fetcher
   A tool for mindfully collecting images from the web

   Please enter the image URL: https://example.com/ubuntu-wallpaper.jpg

   ✓ Successfully fetched: ubuntu-wallpaper.jpg

   ✓ Image saved to Fetched_Images/ubuntu-wallpaper.jpg

   Connection strengthened. Community enriched.


