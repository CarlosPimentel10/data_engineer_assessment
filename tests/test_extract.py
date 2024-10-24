import pytest
import requests
from unittest.mock import patch
from config.config import BASE_URL
from data_engineer_assessment.extract.extract import Extract
import os
import time


class TestExtract():

    def test_source_url(self):
        url = BASE_URL
        response = requests.get(url)
        assert response.status_code == 200

    
    def test_download_xml(self, mocker):
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        mock_response.content = b"<root><child>Test case</child></root>"

        mocker.patch('requests.get', return_value=mock_response)

        extract = Extract()
        result = extract.download_xml()

        assert result is True

        # mocker.patch("requests.get", return_value=mock_response)
        requests.get.assert_called_once_with(extract.url)

        with open('esma_europa.xml', 'rb') as f:
            file_content = f.read()
            assert file_content == mock_response.content
        # Delay before cleanup to ensure file created
        time.sleep(10)

        if os.path.exists('esma_europa.xml'):
            os.remove('esma_europa.xml')



