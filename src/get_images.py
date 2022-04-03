from image_downloader import Downloader

response = Downloader.simple_image_download()
response.download("bear supermario", limit=5)

for url in response.cache:
    print(url)

