from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from typing import Tuple
import time

from constants import AppConstants

Locator = Tuple[By, str]
WaitLocator = Tuple[str, str]


class ElementUtil:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, locator: Locator):
        """
        To find web element
        :param locator: The locator of the element
        :return: WebElement
        """
        return self.driver.find_element(*locator)

    def find_elements(self, locator: Locator):
        """
         To find list of all the web elements
        :param locator: The locator of the element
        :return: List of WebElements
        """
        return self.driver.find_elements(*locator)

    def flashElement(self, locator: Locator):
        """
        Using javascript executor to highlight the web element
        :param locator: The locator of the element
        """
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].style.background='green'", element)
        time.sleep(0.3)

    def click_on_element(self, locator: Locator):
        """
        To click on the web element
        :param locator: The locator of the element
        :return: None
        """
        self.flashElement(locator)
        element = self.find_element(locator)
        element.click()

    def send_keys_to_element(self, locator: Locator, text: str):
        """
        Send keys to the input field
        :param locator: The locator of the element
        :param text: text to be sent to the input field
        """
        element = self.find_element(locator)
        element.send_keys(text)

    def get_text_of_element(self, locator: Locator):
        """
        To get the text of the web element
        :param locator: The locator of the element
        :return: text of the web element
        """
        self.flashElement(locator)
        element = self.find_element(locator)
        return element.text

    def selectByVisibleText(self, locator: Locator, visible_text):
        """
        Handling sort filter dropdown using Select class
        :param locator: The locator of the element
        :param visible_text: text of the web element of the sort option
        """
        element = self.find_element(locator)
        select = Select(element)
        select.select_by_visible_text(visible_text)

    def waitForElementVisible(self, wait_locator: WaitLocator):
        """
        To wait for the element to present on the web page
        :param wait_locator: locator
        """
        wait = WebDriverWait(self.driver, AppConstants.DEFAULT_WAIT, poll_frequency=2, ignored_exceptions=[Exception])
        wait.until(ec.presence_of_element_located(wait_locator))
