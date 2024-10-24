from urllib import response
from config.config import BASE_URL
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


class Extract():

    """This is the starting point to parse the url, confirm success response and write xml file to local system"""

    def __init__(self) -> None:
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
            with open('esma_europa.xml', 'wb') as local_file:
                local_file.write(response.content)

            return True
        else:
            f'Failed to download xml {response.status_code}'
            return False
