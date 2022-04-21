from requests.utils import quote

class ImageFetcher:

    def __init__(self, keyword):
        self.keyword = keyword
        self.url = None

    def make_url(self):
        url = "https://www.google.co.in/search?q={}&source=lnms&tbm=isch".format(self.keyword)
        url = url.replace(" ", "%")
        self.url = url

    def get_images_links(self)
        None

    def download_image(self):
        None
