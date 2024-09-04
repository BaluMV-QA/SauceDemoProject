from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from utils.ElementUtil import ElementUtil


class CheckoutPage(ElementUtil):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.subtotal = (By.CLASS_NAME, "summary_subtotal_label")
        self.finish_button = (By.ID, "finish")

    def enter_shipping_details(self, firstname, lastname, postalcode):
        """
        Enter the shipping details
        :param firstname: firstname
        :param lastname: lastname
        :param postalcode: postal code
        """
        self.waitForElementVisible(self.first_name)
        self.send_keys_to_element(self.first_name, firstname)
        self.send_keys_to_element(self.last_name, lastname)
        self.send_keys_to_element(self.postal_code, postalcode)

    def click_on_continue_button(self):
        """ Click on Continue button, takes the user to shipping overview page"""
        self.click_on_element(self.continue_button)

    def get_subtotal(self):
        """
        Get the subtotal from the shipping page
        :return: subtotal
        """
        self.waitForElementVisible(self.subtotal)
        total = self.get_text_of_element(self.subtotal)
        return total.split("$")[1]

    def click_on_finish_button(self):
        """
        Click on finish button,user is navigated to order confirmation page
        """
        self.click_on_element(self.finish_button)
