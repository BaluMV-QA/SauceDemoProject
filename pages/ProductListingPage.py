"""  POM of the product listing page (PLP) """
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from constants import AppConstants
from utils.ElementUtil import ElementUtil


class ProductListingPage(ElementUtil):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.title = (By.CLASS_NAME, "title")
        self.product = (By.CLASS_NAME, "inventory_item_name")
        self.products_price = (By.CLASS_NAME, "inventory_item_price")
        self.sort_dropdown = (By.CLASS_NAME, "product_sort_container")
        self.mini_cart = (By.CLASS_NAME, "shopping_cart_link")
        self.burger_menu = (By.ID,"react-burger-menu-btn")
        self.logout_link = (By.ID,"logout_sidebar_link")

    def get_title(self):
        """
        Get the page title of the PLP page
        :return:  title
        """
        self.waitForElementVisible(self.title)
        return self.get_text_of_element(self.title)

    def get_current_url(self):
        """
        Get the url of the PLP page
        :return: url
        """
        return self.driver.current_url

    def get_products_price(self):
        """
        Get the price of all products on the PLP.
        :return: Prices of all the products
        """
        product_prices = self.find_elements(self.products_price)
        return [float(item.text.replace("$", "")) for item in product_prices]

    def sort_prices_low_to_high(self):
        """
        Logic to sort list of prices using lambda function
        :return: sorted prices in ascending order
        """
        prices = self.get_products_price()
        return sorted(prices, key=lambda x: x)

    def sort_prices_high_to_low(self):
        """
        Logic to sort list of prices using lambda function
        :return: sorted prices in descending order
        """
        prices = self.get_products_price()
        return sorted(prices, key=lambda x: x, reverse=True)

    def apply_sort_filter(self, visible_text):
        """
        Using Select class to select the price filter from the sort dropdown
        :param visible_text: filter name
        """
        self.selectByVisibleText(self.sort_dropdown, visible_text)

    def add_products_to_cart(self):
        """
        Add multiple products to cart,
        dynamic xpath is used to pass the title of the products that needs to be added to the cart
        """
        product_titles = AppConstants.PRODUCT_TITLES
        for product in product_titles:
            self.driver.find_element(By.XPATH,
                                     "//div[text()=" + product + "]/ancestor::div/following-sibling::div//button").click()

    def click_on_mini_cart(self):
        """
        Click on mini cart, user navigated to cart page
        """
        self.click_on_element(self.mini_cart)

    def click_on_burger_menu(self):
        """
        Click on burger menu
        """
        self.click_on_element(self.burger_menu)

    def click_on_logout_link(self):
        """
        Click on logout link
        """
        self.click_on_element(self.logout_link)