"""  POM of the Login page """
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from utils.ElementUtil import ElementUtil


class LoginPage(ElementUtil):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.XPATH, '//h3[@data-test="error"]')

    def input_username(self, username):
        """ Enter a username into the username textbox. """
        self.send_keys_to_element(self.username, username)

    def input_password(self, password):
        """ Enter a password into the password textbox. """
        self.send_keys_to_element(self.password, password)

    def click_on_login_button(self):
        """ click on Login button. """
        self.click_on_element(self.login_button)

    def user_login(self, username, password):
        """ perform user login. """
        self.input_username(username)
        self.input_password(password)
        self.click_on_login_button()

    def get_error_message(self):
        """
        Get the error message if username/password is incorrect.
        :return: error message on Login failed
        """
        return self.get_text_of_element(self.error_message)

    def get_current_url(self):
        """
        Get the url of the Login page
        :return: url
        """
        return self.driver.current_url

    def check_if_username_field_is_displayed(self):
        """
        To check if username text field is displayed
        :return: True if element is displayed
        """
        return self.element_displayed(self.username)

    def check_if_password_field_is_displayed(self):
        """
        To check if password text field is displayed
        :return: True if element is displayed
        """
        return self.element_displayed(self.password)


