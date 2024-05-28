import allure

from selene import browser, query
from pages.open_page import open_page

from utils.helper import api_request


class Cart:

    def add_item(self, url, endpoint, cookie_customer):
        open_page.open_start_page(url)

        with allure.step("Отправляется запрос к API на добавление продукта в корзину"):
            response = api_request(url, endpoint, "POST", cookies={'Nop.customer': cookie_customer})

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
            response = api_request(
                url,
                endpoint,
                method="POST",
                data=payload,
                cookies={'Nop.customer': cookie_customer}
            )

        open_page.open_cart_page(url)

        return response


cart = Cart()
