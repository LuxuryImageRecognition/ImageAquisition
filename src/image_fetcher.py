import requests
import urllib.request
import os
import ssl
from requests.utils import quote
from bs4 import BeautifulSoup

class ImageFetcher:

    def __init__(self):
        self.url = None
        self.img_urls = []

    def make_url(self, brand, model):
        url = "https://www.google.co.in/search?q={} {}&source=lnms&tbm=isch".format(brand, model)
        url = url.replace(" ", "%")
        self.url = url
        print(url)

    def get_images_links(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        image_tags = soup.find_all('img', class_ = "yWs4tf")

        for image_tag in image_tags:
            print(image_tag["src"])
            self.img_urls.append(image_tag["src"])


    def download_images(self, output_folder):
        for url in self.img_urls:
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            image_name = url.split("tbn:")[1]
            urllib.request.urlretrieve(url, "images/{}.jpg".format(image_name))



