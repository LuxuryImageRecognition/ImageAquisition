from requests.utils import quote

class ImageFetcher:

    def __init__(self):
        self.url = None

    def make_url(self, brand, model):
        url = "https://www.google.co.in/search?q={} {}&source=lnms&tbm=isch".format(brand, model)
        url = url.replace(" ", "%")
        self.url = url

    def get_images_links(self):
        None

    def download_image(self):
        None
