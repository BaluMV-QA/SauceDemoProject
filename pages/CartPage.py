from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from utils.ElementUtil import ElementUtil


class CartPage(ElementUtil):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.product_title = (By.CLASS_NAME, "inventory_item_name")
        self.mini_cart_count = (By.CLASS_NAME, "shopping_cart_badge")
        self.products_price = (By.CLASS_NAME, "inventory_item_price")
        self.checkout_button = (By.ID, "checkout")

    def product_count_on_mini_cart(self):
        """
        Get product count in the mini cart
        :return: count
        """
        self.waitForElementVisible(self.mini_cart_count)
        return self.get_text_of_element(self.mini_cart_count)

    def get_product_title_in_cart(self):
        """
        Get the titles of the products present in the cart.
        :return: product titles
        """
        product_titles = self.find_elements(self.product_title)
        product_names = []
        for product in product_titles:
            product_names.append(product.text)
        return product_names

    def calculate_cart_total(self):
        """
        Get all prices on the cart page and return their sum.
        :return: cart total
        """
        prices = self.find_elements(self.products_price)
        total = 0.0
        for price in prices:
            product_price = float(price.text.replace("$", ""))
            total += product_price
        return total

    def click_on_checkout(self):
        """ Click the checkout button. (Goes to the checkout page.) """
        self.click_on_element(self.checkout_button)
