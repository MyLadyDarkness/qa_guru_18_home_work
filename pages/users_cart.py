import json
import allure
import requests

from allure_commons.types import AttachmentType
from selene import browser, query
from pages.open_pages import open_page

import logging


class Cart:

    def add_item(self, url, endpoint, cookie_customer):
        open_page.open_start_page(url)

        with allure.step("Отправляется запрос к API на добавление продукта в корзину"):
            response = requests.post(url + endpoint, cookies={'Nop.customer': cookie_customer})

        allure.attach(body=json.dumps(response.json(), indent=4, ensure_ascii=True), name="Response",
                      attachment_type=AttachmentType.JSON, extension="json")

        logging.info(response.request.url)
        logging.info(response.status_code)
        logging.info(response.text)

        with allure.step("Куки добавляются в браузер"):
            browser.driver.add_cookie({"name": "Nop.customer", "value": cookie_customer})

        open_page.open_cart_page(url)

        return response

    def delete_item(self, url, endpoint, cookie_customer):
        with allure.step("Получение ID продукта"):
            item_id = browser.element(".remove-from-cart input[type=checkbox]").get(query.value)

        payload = {
            'removefromcart': item_id,
            'updatecart': 'Update shopping cart'
        }

        with allure.step("Отправляется запрос к API на удаление продукта из корзины"):
            response = requests.post(
                url + endpoint,
                data=payload,
                cookies={'Nop.customer': cookie_customer}
            )

        allure.attach(body=response.text, name="HTML", attachment_type=AttachmentType.HTML, extension="html")

        logging.info(response.request.url)
        logging.info(response.status_code)
        logging.info(response.text)

        open_page.open_cart_page(url)

        return response


cart = Cart()
