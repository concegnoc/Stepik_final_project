from .base_page import BasePage
from .locators import BasketPageLocators
import time

class BasketPage(BasePage):
    def should_check_condition_of_basket(self):
        assert self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_LINK), "The basket is not empty"
