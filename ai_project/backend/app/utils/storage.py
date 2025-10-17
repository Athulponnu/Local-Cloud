import os
import shutil

STORAGE_PATH = "storage/images"

def save_image(file_path: str):
    """
    Copy uploaded image into the local storage folder
    """
    os.makedirs(STORAGE_PATH, exist_ok=True)
    filename = os.path.basename(file_path)
    dest = os.path.join(STORAGE_PATH, filename)
    shutil.copy(file_path, dest)
    print(f"✅ Image saved to {dest}")
    return dest

if __name__ == "__main__":
    test_img = "test.jpg"  # replace with any sample file
    if os.path.exists(test_img):
        save_image(test_img)
    else:
        print("⚠️ No test image found.")
