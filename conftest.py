from urllib2 import urlopen

import pytest
from bs4 import BeautifulSoup

def pytest_addoption(parser):
    parser.addoption("--url", action="store",
        help="URL to check")

@pytest.fixture
def url(request):
    return request.config.getoption("--url")

@pytest.fixture
def soup(request):
    soup.cache = (soup.cache or BeautifulSoup(urlopen(request.config.getoption("--url"))))
    return soup.cache
soup.cache = None
