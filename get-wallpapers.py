import requests
import os
import re
from requests_html import HTMLSession

url = "https://wallpaperaccess.com/anime-pc"
url_home = url[:-9]

try:

    relative_images_dir = "~/Downloads/images/"
    save_dir = os.path.expanduser(relative_images_dir)
    session = HTMLSession()
    body = session.get(url)
    images = body.html.find("img")
    pattern = r"data-src='(.*?)'"
    image_links = [str(image_link) for image_link in images if "data-src" in str(image_link)]
    extracted_data = []
    for i in image_links:
        match = re.search(pattern, i)
        if match:
            extracted_data.append(url_home + match.group(1))
    print(extracted_data)
    for i, image_url in enumerate(extracted_data, start=1):
        try:
            image_response = requests.get(image_url)
            image_response.raise_for_status()

            image_name = os.path.join(save_dir, f"image{i}.jpg")
                #if width > height:
            with open(image_name, 'wb') as image_file:
                image_file.write(image_response.content)
            print(f"Image {i} downloaded successfully.")
               # else:
               #     print(f"Image {i} does not meet the criteria (width is not longer than height). Skipping.")
        except (IOError, requests.exceptions.RequestException) as e:
            print(f"Failed to download Image {i}: {e}")
except Exception as e:
    print(e)
