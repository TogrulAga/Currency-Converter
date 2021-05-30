import requests


def get_content_type(url):
    return requests.get(url=url).headers["content-type"]
