import allure
import pytest

from constants import AppConstants
from pages.LoginPage import LoginPage
from pages.ProductListingPage import ProductListingPage


@pytest.mark.usefixtures("driver", "log_on_failure")
class TestProductListing:

    @allure.epic("Epic2: Filter Products by Price (Low to High)")
    @allure.feature("TC#1 - Sort products by price using low to high filter on PLP")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Filter Products by Price (Low to High)")
    @pytest.mark.regression
    @pytest.mark.order(2)
    def test_sort_products_by_price_low_to_high(self):
        # Login using valid user credentials, reading the user data from the constants file
        login_page = LoginPage(self.driver)
        login_page.user_login(AppConstants.STANDARD_USER, AppConstants.STANDARD_PASSWORD)

        # On the PLP page apply the sort low to high price filter and assert the sorted price
        product_listing_page = ProductListingPage(self.driver)
        expected_price = product_listing_page.sort_prices_low_to_high()
        product_listing_page.apply_sort_filter(AppConstants.LOW_TO_HIGH)
        actual_price = product_listing_page.get_products_price()
        assert actual_price == expected_price, f"Expected {expected_price} but got {actual_price}"

    @allure.epic("Epic2: Filter Products by Price (High to Low)")
    @allure.feature("TC#2 - Sort products by price using high to low filter on PLP")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Filter Products by Price (High to Low)")
    @pytest.mark.regression
    @pytest.mark.order(3)
    def test_sort_products_by_price_high_to_low(self):
        # Login using valid user credentials, reading the user data from the constants file
        login_page = LoginPage(self.driver)
        login_page.user_login(AppConstants.STANDARD_USER, AppConstants.STANDARD_PASSWORD)

        # On the PLP page apply the sort high to low price filter and assert the sorted price
        product_listing_page = ProductListingPage(self.driver)
        expected_price = product_listing_page.sort_prices_high_to_low()
        product_listing_page.apply_sort_filter(AppConstants.HIGH_TO_LOW)
        actual_price = product_listing_page.get_products_price()
        assert actual_price == expected_price, f"Expected {expected_price} but got {actual_price}"
