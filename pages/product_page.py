from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_product_in_basket(self):
        #self.add_item_to_busket()
        #self.solve_quizes_and_get_code()
        self.should_have_same_name()
        self.should_have_same_price()

    def solve_quizes_and_get_code(self):
        self.solve_quiz_and_get_code()

    def add_item_to_busket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_have_same_name(self):
        expected_name = self.browser.find_element(*ProductPageLocators.EXPECTED_NAME).text
        actual_name = self.browser.find_element(*ProductPageLocators.ACTUAL_NAME).text
        assert actual_name == expected_name, "Name of added item is not equal to expected"

    def should_have_same_price(self):
        expected_price = self.browser.find_element(*ProductPageLocators.EXPECTED_NAME).text
        actual_price = self.browser.find_element(*ProductPageLocators.ACTUAL_NAME).text
        assert actual_price == expected_price, "Price of added item is not equal to expected"
