from urllib import response
from config.config import BASE_URL
import requests
from bs4 import BeautifulSoup
import pandas as pd 
import numpy as np

class Extract():

    def __init__(self) -> None:
        pass


    def source_url(self):
        url = BASE_URL
        response = requests.get(url)
        if response.status_code == 200:
            return response
        else:
            raise Exception(f'Failed to get data from source url ${response.status_code}')
    
    def download_xml(self):
        response = requests.get(BASE_URL)
        soup = BeautifulSoup(response.content, 'lxml')
