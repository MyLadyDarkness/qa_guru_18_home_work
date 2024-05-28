from pages.users_cart import cart
from selene import browser, have

from tests.conftest import BASE_URL


def test_add_cart_one_item(cookie_customer):
    endpoint = "/addproducttocart/catalog/13/1/1"
    response = cart.add_item(BASE_URL, endpoint, cookie_customer=cookie_customer)
    assert response.status_code == 200

    browser.element(".product-name").should(have.text("Computing and Internet"))
    browser.element(".qty-input").should(have.value("1"))


def test_add_cart_item_twice(cookie_customer):
    endpoint = "/addproducttocart/catalog/22/1/1"

    response = cart.add_item(BASE_URL, endpoint, cookie_customer=cookie_customer)
    assert response.status_code == 200

    response = cart.add_item(BASE_URL, endpoint, cookie_customer=cookie_customer)
    assert response.status_code == 200

    browser.element(".product-name").should(have.text("Health Book"))
    browser.element(".qty-input").should(have.value("2"))


def test_delete_from_cart(cookie_customer):
    endpoint1 = "/addproducttocart/catalog/22/1/1"
    endpoint2 = "/cart"

    cart.add_item(BASE_URL, endpoint1, cookie_customer=cookie_customer)
    response = cart.delete_item(BASE_URL, endpoint2, cookie_customer=cookie_customer)

    assert response.status_code == 200
    browser.element(".cart-qty").should(have.text("0"))
