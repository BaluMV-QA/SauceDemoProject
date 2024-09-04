import allure
import pytest

from constants import AppConstants
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
from pages.LoginPage import LoginPage
from pages.OrderConfirmationPage import OrderConfirmationPage
from pages.ProductListingPage import ProductListingPage


@pytest.mark.usefixtures("driver", "log_on_failure")
class TestCheckout:
    @allure.epic("Epic5: Order Placement")
    @allure.feature("TC#1 - Verify Order Confirmation by placing an order")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("Verify Order Confirmation by placing an order")
    @pytest.mark.smoke
    @pytest.mark.order(6)
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
        cart_page.click_on_checkout()

        # On checkout page, enter the shipping details and click on finish button
        checkout_page = CheckoutPage(self.driver)
        checkout_page.enter_shipping_details(AppConstants.FIRST_NAME, AppConstants.LAST_NAME, AppConstants.POSTAL_CODE)
        checkout_page.click_on_continue_button()
        checkout_page.click_on_finish_button()

        # User is navigated to the order confirmation page, assert the order success message and the page title
        order_confirmation_page = OrderConfirmationPage(self.driver)
        order_success_message = order_confirmation_page.get_order_success_message()
        assert order_success_message == AppConstants.ORDER_SUCCESS_MESSAGE, f"Expected {AppConstants.ORDER_SUCCESS_MESSAGE} but got {order_success_message}"
        assert order_confirmation_page.get_title() == AppConstants.ORDER_CONFIRMATION_PAGE_TITLE, f"Expected {AppConstants.ORDER_CONFIRMATION_PAGE_TITLE} but got {order_confirmation_page.get_title()}"
