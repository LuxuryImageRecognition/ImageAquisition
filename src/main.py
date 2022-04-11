from tkinter import image_names
import requests
import urllib.request
from PIL import Image
from bs4 import BeautifulSoup

URL = "https://www.google.com/search?q=alma+bag+louis+vuitton&tbm=isch&ved=2ahUKEwi8wtqU0oz3AhUI3RoKHRwTBLAQ2-cCegQIABAA&oq=alma+bag&gs_lcp=CgNpbWcQARgBMgUIABCABDIECAAQHjIECAAQHjIECAAQHjIECAAQHjIECAAQHjIECAAQHjIECAAQHjIECAAQHjIECAAQHjoKCCMQ7wMQ6gIQJzoHCCMQ7wMQJzoECAAQQzoICAAQsQMQgwE6CAgAEIAEELEDOgQIABADOgsIABCABBCxAxCDAVDzBViZF2DAJmgBcAB4AIABN4gBrQOSAQE5mAEAoAEBqgELZ3dzLXdpei1pbWewAQrAAQE&sclient=img&ei=tXNUYvyTKIi6a5ymkIAL"

page = requests.get(URL)


soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())
image_tags = soup.find_all('img')
links = []
for image_tag in image_tags:
    links.append(image_tag['src'])

links = links[1:]
print(links[0])
urllib.request.urlretrieve(links[0], "images/alma_bag.jpg")

for link in links:
    image_name = link.split("tbn:")[1]
    urllib.request.urlretrieve(link, "images/{}.jpg".format(image_name))




























