from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_add_product_in_basket(self):
        product = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_TO_BASKET)
        product.click()

    def should_compare_price_in_basket(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT)
        adding_price = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT_IN_BASKET)
        assert price.text == adding_price.text, "Product price in basket must be equal to product price"

    def should_compare_product_name(self):
        name = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT)
        adding_name = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT_IN_BASKET)
        assert name.text == adding_name.text, "Adding product name must be equal to product name"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not presented, but should be"