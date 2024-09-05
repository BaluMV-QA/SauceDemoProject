import allure
import pytest

from constants import AppConstants
from pages.LoginPage import LoginPage
from pages.ProductListingPage import ProductListingPage


@pytest.mark.usefixtures("driver", "log_on_failure")
class TestLogin:

    @allure.epic("Epic1: Login and logout feature")
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

    @allure.epic("Epic1: Login and logout feature")
    @allure.feature("TC#2 - Login with invalid user credentials(negative test)")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    @allure.title("Login with invalid user credentials")
    @pytest.mark.smoke
    @pytest.mark.order(2)
    def test_invalid_login(self):
        """
        Test login feature using invalid credentials
        """
        # User login with invalid username and password
        login_page = LoginPage(self.driver)
        login_page.input_username(AppConstants.INVALID_USER)
        login_page.input_password(AppConstants.STANDARD_PASSWORD)
        login_page.click_on_login_button()

        # Verify if the error message is displayed on entering the invalid user name
        error_message = login_page.get_error_message()
        assert error_message == AppConstants.INVALID_USER_LOGIN_FAILED, f"Expected error message, but got '{error_message}'"

    @allure.epic("Epic1: Login and logout feature")
    @allure.feature("TC#3 - Login with locked-out user credentials(negative test)")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    @allure.title("Login with locked-out user credentials")
    @pytest.mark.smoke
    @pytest.mark.order(3)
    def test_locked_out_user_login(self):
        """
        Test login feature using invalid credentials
        """
        # User login with locked out username and password
        login_page = LoginPage(self.driver)
        login_page.input_username(AppConstants.LOCKED_OUT_USER)
        login_page.input_password(AppConstants.STANDARD_PASSWORD)
        login_page.click_on_login_button()

        # Verify if the error message is displayed on entering the invalid locked out username
        error_message = login_page.get_error_message()
        assert error_message == AppConstants.LOCKED_OUT_USER_LOGIN_FAILED, f"Expected error message, but got '{error_message}'"

    @allure.epic("Epic1: Login and logout feature")
    @allure.feature("TC#4 - Verify logout is successful")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Verify logout is successful")
    @pytest.mark.smoke
    @pytest.mark.order(4)
    def test_logout(self):
        # Login using valid user credentials, reading the user data from the constants file
        login_page = LoginPage(self.driver)
        login_page.input_username(AppConstants.STANDARD_USER)
        login_page.input_password(AppConstants.STANDARD_PASSWORD)
        login_page.click_on_login_button()

        # On PLP page , click on burger menu and the click on logout link
        product_listing_page = ProductListingPage(self.driver)
        product_listing_page.click_on_burger_menu()
        product_listing_page.click_on_logout_link()

        # Asserting the Page url and username and password is displayed
        assert login_page.get_current_url() == AppConstants.URL, "Logout was not successful"
        assert login_page.check_if_username_field_is_displayed() == True, "Logout was not successful"
        assert login_page.check_if_password_field_is_displayed() == True, "Logout was not successful"
