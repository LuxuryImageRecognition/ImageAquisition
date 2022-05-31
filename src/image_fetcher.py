import glob
import os
import ssl
import urllib.request

from bs4 import BeautifulSoup
from google.cloud import storage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class ImageFetcher:
    ssl._create_default_https_context = ssl._create_unverified_context

    def __init__(self):
        self.url = None
        self.img_urls = []

    def make_url(self, brand, model):
        url = "https://www.google.co.in/search?q={} {}&source=lnms&tbm=isch".format(brand, model)
        url = url.replace(" ", "%")
        self.url = url
        print(url)

    def get_html(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(self.url)
        html = driver.page_source
        return html

    def get_images_links(self):
        self.img_urls = []
        html = self.get_html()
        print("Get HTML from url")
        soup = BeautifulSoup(html, 'html.parser')
        image_tags = soup.find_all('img')

        for image_tag in image_tags:
            try:
                self.img_urls.append(image_tag["src"])
            except KeyError:
                try:
                    self.img_urls.append(image_tag["data-src"])
                except KeyError:
                    print("Neither src or data-src was found in the tag")
        print("{} images urls has been found".format(len(self.img_urls)))

    def download_images(self, output_folder, bag_name):
        image_id = 0
        for url in self.img_urls:
            image_id = image_id + 1
            bag_path = "{}/{}".format(output_folder, bag_name)
            if not os.path.exists(bag_path):
                os.makedirs(bag_path)
            urllib.request.urlretrieve(url, "images/{}/img_{}.jpg".format(bag_name, image_id))

    def export_gcs(self, bucket, bag_name):
        client = storage.Client()
        source_bucket = client.get_bucket(bucket)
        all_img_paths = glob.glob("images/{}/*".format(bag_name))
        for path in all_img_paths:
            blob = source_bucket.blob("raw/" + path.replace("images/", ""))
            blob.upload_from_filename(path)
