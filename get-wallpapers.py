import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from PIL import Image
import io

def download_images_with_longer_width(url, save_dir):
    try:
        response = requests.get(url)

        soup = BeautifulSoup(response.content, 'html.parser')

        image_tags = soup.find_all('img')
        image_urls = [urljoin(url, img['src']) for img in image_tags if 'src' in img.attrs]

        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        for i, image_url in enumerate(image_urls, start=1):
            try:
                image_response = requests.get(image_url)
                image_response.raise_for_status()

                image = Image.open(io.BytesIO(image_response.content))
                width, height = image.size

                if width > height:
                    with open(image_name, 'wb') as image_file:
                        image_file.write(image_response.content)

                    print(f"Image {i} downloaded successfully.")
                else:
                    print(f"Image {i} does not meet the criteria (width is not longer than height). Skipping.")
            except (IOError, requests.exceptions.RequestException) as e:
                print(f"Failed to download Image {i}: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")

if __name__ == "__main__":

    relative_images_dir="~/Downloads/images"
    save_directory = os.path.expanduser(relative_images_dir)

    webpage_url = "http://m.gettywallpapers.com/cool-anime-wallpapers/"

    download_images_with_longer_width(webpage_url, save_directory)

