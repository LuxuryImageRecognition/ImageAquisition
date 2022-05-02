from src.image_fetcher import ImageFetcher

fetcher = ImageFetcher()

def test_make_url():
    fetcher.make_url("louis vuitton", "alma bag")
    expected_url = "https://www.google.co.in/search?q=louis%vuitton%alma%bag&source=lnms&tbm=isch"
    assert fetcher.url == expected_url