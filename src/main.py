from image_fetcher import ImageFetcher
import json

with open("bags.json") as bag_conf_file:
    bags_conf = json.loads(bag_conf_file.read())

fetcher = ImageFetcher()

for conf in bags_conf:
    print(conf)
    fetcher.make_url(conf["brand"], conf["model"])
    #fetcher.get_images_links()
    bag_name = "{}_{}".format(conf["brand"], conf["model"])
    #fetcher.download_images("images", bag_name)
    fetcher.export_gcs("image_cleaning", bag_name)

