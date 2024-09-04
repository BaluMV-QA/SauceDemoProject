import allure
import pytest

from constants import AppConstants
from pages.CartPage import CartPage
from pages.LoginPage import LoginPage
from pages.ProductListingPage import ProductListingPage


@pytest.mark.usefixtures("driver", "log_on_failure")
class TestCart:

    @allure.epic("Epic3: Add Multiple Products to Cart")
    @allure.feature("TC#1 - Select multiple products and add them to the cart.")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("Add multiple products to cart test")
    @pytest.mark.smoke
    @pytest.mark.order(4)
    def test_add_products_to_cart(self):
        # Login using valid user credentials, reading the user data from the constants file
        login_page = LoginPage(self.driver)
        login_page.user_login(AppConstants.STANDARD_USER, AppConstants.STANDARD_PASSWORD)

        # On the product listing page , add two products to cart, click on mini cart
        product_listing_page = ProductListingPage(self.driver)
        product_listing_page.add_products_to_cart()
        product_listing_page.click_on_mini_cart()

        # User gets navigated to cart page, assert the product count on the mini cart and products added to the cart
        cart_page = CartPage(self.driver)
        mini_cart_product_count = cart_page.product_count_on_mini_cart()
        assert mini_cart_product_count == "2", f"Expected 2 but got {mini_cart_product_count}"
        assert cart_page.get_product_title_in_cart() == AppConstants.PRODUCT_NAMES, f"Expected {AppConstants.PRODUCT_NAMES} but got {cart_page.get_product_title_in_cart()} "
