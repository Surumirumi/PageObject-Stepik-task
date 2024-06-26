from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def open_busket(self):
        OPEN_BUSKET_BUTTON = self.browser.find_element(*BasketPageLocators.OPEN_BUSKET_BUTTON)
        OPEN_BUSKET_BUTTON.click()
    
    def busket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BUSKET_ITEMS), "Busket is not empty"
    
    def empty_basket_should_have_cap(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_CAP), "There is no visible busket cap"