import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


SBIS_MAIN_PAGE_URL = "https://sbis.ru/"
TENSOR_MAIN_PAGE_URL = "https://tensor.ru/"


logging.basicConfig(level=logging.INFO)


@pytest.fixture(scope='function')
def browser():
    service = Service()
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": 'C:\\Users\\Alex\\Python\\Tensor_SBIS\\download',
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }

    options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(service=service, options=options)

    driver.maximize_window()
    yield driver
    driver.quit()
