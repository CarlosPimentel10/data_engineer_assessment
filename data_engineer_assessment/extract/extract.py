from urllib import response
from config.config import BASE_URL
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


class Extract():

    def __init__(self, url) -> None:
        self.url = BASE_URL

    def source_url(self):
        url = self.BASE_URL
        response = requests.get(url)
        if response.status_code == 200:
            return response
        else:
            raise Exception(
                f'Failed to get data from source url ${response.status_code}')

    def download_xml(self):
        response = requests.get(self.BASE_URL)
        if response.status_code == 200:
            with open(BASE_URL, 'wb') as local_file:
                soup = BeautifulSoup(response.content, 'lxml')
                local_file.write(response.content)
