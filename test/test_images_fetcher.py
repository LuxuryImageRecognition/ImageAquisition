from src.image_fetcher import ImageFetcher

fetcher = ImageFetcher("louis vuitton")

def test_make_url():
    fetcher.make_url()
    expected_url = "https://www.google.co.in/search?q=louis%vuitton&source=lnms&tbm=isch"
    assert fetcher.url == expected_url