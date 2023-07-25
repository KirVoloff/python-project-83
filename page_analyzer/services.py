import logging

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def get_correct_url(url: str) -> str:
    url = urlparse(url)
    return url._replace(
        path='',
        params='',
        query='',
        fragment='').geturl()


def parse_page(url):
    page_data = {
        'h1': '',
        'title': '',
        'description': ''
    }
    response = get_response(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    h1 = soup.h1
    title = soup.title
    content = soup.find("meta", attrs={'name': 'description'})

    page_data['h1'] = h1.get_text() if h1 else ''
    page_data['title'] = title.get_text() if title else ''
    page_data['description'] = content["content"] if content else ''

    return page_data


def get_response(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response
    except Exception as err:
        logging.error(err)
