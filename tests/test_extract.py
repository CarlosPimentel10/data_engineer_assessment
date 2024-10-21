from urllib import response
import pytest
import requests
from config.config import BASE_URL


class TestExtract():
    
    def test_source_url(self):
        url = BASE_URL
        response = requests.get(url)
        assert response.status_code == 200
    
    def test_download_xml():
        pass


test_extract = TestExtract()
test_extract.test_source_url()