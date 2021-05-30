import requests


def check_success(url):
    r = requests.get(url=url)
    return "Success" if r else "Fail"
