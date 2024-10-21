import pytest
import requests
import os


class TestExtract():
    
    def __init__(self, url) -> None:
        self.url = url

    def test_source_url(self):
        url = ""
