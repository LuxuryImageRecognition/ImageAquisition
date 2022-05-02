
import requests
import urllib.request
import os
import ssl

from bs4 import BeautifulSoup

URL = "https://www.google.com/search?q=alma+bag+louis+vuitton&tbm=isch&ved=2ahUKEwi8wtqU0oz3AhUI3RoKHRwTBLAQ2-cCegQIABAA&oq=alma+bag&gs_lcp=CgNpbWcQARgBMgUIABCABDIECAAQHjIECAAQHjIECAAQHjIECAAQHjIECAAQHjIECAAQHjIECAAQHjIECAAQHjIECAAQHjoKCCMQ7wMQ6gIQJzoHCCMQ7wMQJzoECAAQQzoICAAQsQMQgwE6CAgAEIAEELEDOgQIABADOgsIABCABBCxAxCDAVDzBViZF2DAJmgBcAB4AIABN4gBrQOSAQE5mAEAoAEBqgELZ3dzLXdpei1pbWewAQrAAQE&sclient=img&ei=tXNUYvyTKIi6a5ymkIAL"
OUTPUT_FOLDER = "images"
page = requests.get(URL)

ssl._create_default_https_context = ssl._create_unverified_context



def download_images(url):
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
    image_name = url.split("tbn:")[1]
    urllib.request.urlretrieve(url, "images/{}.jpg".format(image_name))

soup = BeautifulSoup(page.content, 'html.parser')
image_tags = soup.find_all('img', class_ = "yWs4tf")

for image_tag in image_tags:
    download_images(image_tag['src'])



















