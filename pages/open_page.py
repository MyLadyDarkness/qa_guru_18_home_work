import allure

from selene import browser


class OpenPage:

    def open_start_page(self, url):
        with allure.step("Открывается сайт"):
            browser.open(url)

    def open_cart_page(self, url):
        with allure.step("Открывается корзина"):
            browser.open(url + "/cart")


open_page = OpenPage()
