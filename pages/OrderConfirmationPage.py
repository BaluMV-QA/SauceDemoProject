from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from utils.ElementUtil import ElementUtil


class OrderConfirmationPage(ElementUtil):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.title = (By.CLASS_NAME, "title")
        self.order_success_message = (By.CLASS_NAME, "complete-header")

    def get_title(self):
        """ Get the Order confirmation page title. """
        return self.get_text_of_element(self.title)

    def get_order_success_message(self):
        """ Get the order confirmation success message"""
        self.waitForElementVisible(self.order_success_message)
        return self.get_text_of_element(self.order_success_message)
