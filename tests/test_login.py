import allure
import pytest

from constants import AppConstants
from pages.LoginPage import LoginPage
from pages.ProductListingPage import ProductListingPage


@pytest.mark.usefixtures("driver", "log_on_failure")
class TestLogin:

    @allure.epic("Epic1: Log in using valid credentials")
    @allure.feature("TC#1 - Log in using valid credentials")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("Log in using valid credentials")
    @pytest.mark.smoke
    @pytest.mark.order(1)
    def test_valid_user_login(self):
        # Login using valid user credentials, reading the user data from the constants file
        login_page = LoginPage(self.driver)
        login_page.input_username(AppConstants.STANDARD_USER)
        login_page.input_password(AppConstants.STANDARD_PASSWORD)
        login_page.click_on_login_button()

        # Fetching the page title of the PLP page to assert if the login is successful, also asserting the url
        product_listing_page = ProductListingPage(self.driver)
        title = product_listing_page.get_title()
        assert title == AppConstants.PRODUCT_LANDING_PAGE_TITLE, f"Expected is {AppConstants.PRODUCT_LANDING_PAGE_TITLE} but got {title}"
        assert "inventory" in product_listing_page.get_current_url(), f"Login Failed"
