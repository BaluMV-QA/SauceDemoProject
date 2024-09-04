import allure
import pytest

from constants import AppConstants
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
from pages.LoginPage import LoginPage
from pages.ProductListingPage import ProductListingPage


@pytest.mark.usefixtures("driver", "log_on_failure")
class TestCheckout:
    @allure.epic("Epic4: Proceed to Checkout")
    @allure.feature("TC#1 - Navigate to the cart and proceed to checkout.")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("Proceed to Checkout")
    @pytest.mark.smoke
    @pytest.mark.order(5)
    def test_checkout(self):
        # Login using valid user credentials, reading the user data from the constants file
        login_page = LoginPage(self.driver)
        login_page.user_login(AppConstants.STANDARD_USER, AppConstants.STANDARD_PASSWORD)

        # On the product listing page , add two products to cart, click on mini cart
        product_listing_page = ProductListingPage(self.driver)
        product_listing_page.add_products_to_cart()
        product_listing_page.click_on_mini_cart()

        # User is navigated to cart page , proceed to checkout
        cart_page = CartPage(self.driver)
        cart_total = cart_page.calculate_cart_total()
        cart_page.click_on_checkout()

        # On checkout page, enter the shipping details and assert the subtotal is same as the cart total
        checkout_page = CheckoutPage(self.driver)
        checkout_page.enter_shipping_details(AppConstants.FIRST_NAME, AppConstants.LAST_NAME, AppConstants.POSTAL_CODE)
        checkout_page.click_on_continue_button()
        assert checkout_page.get_subtotal() == str(
            cart_total), f"Expected {cart_page} but got {checkout_page.get_subtotal()}"
