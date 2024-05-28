import allure
import pytest
from selene import browser

from utils.helper import api_request

BASE_URL = 'https://demowebshop.tricentis.com'


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = BASE_URL
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    browser.quit()


@pytest.fixture(scope='function', autouse=False)
def cookie_customer():
    with allure.step('Получение cookie посетителя'):
        result = api_request(url=BASE_URL, endpoint="", method="GET")
        cookie_customer = result.cookies.get('Nop.customer')

    yield cookie_customer
