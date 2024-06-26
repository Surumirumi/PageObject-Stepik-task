from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ACTUAL_NAME = (By.XPATH, "//div[@id='messages']/div[1]//strong")
    EXPECTED_NAME = (By.XPATH, "//div[contains(@class,'product_main')]/h1")
    ACTUAL_PRICE = (By.XPATH, "//div[@id='messages']/div[3]//strong")
    EXPECTED_PRICE = (By.CSS_SELECTOR, ".price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class BasketPageLocators():
    OPEN_BUSKET_BUTTON = (By.XPATH, "//span/a[contains(@class,'btn-default')]")
    BUSKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_CAP = (By.XPATH, "//div[@id='content_inner']/p")