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
