from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    EMAIL_FOR_REG_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FOR_REG_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
    REPEATING_PASSWORD_FOR_REG_FORM = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.XPATH, "//button[@value='Register']")

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
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    OPEN_BUSKET_BUTTON = (By.XPATH, "//span/a[contains(@class,'btn-default')]")
    BUSKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_CAP = (By.XPATH, "//div[@id='content_inner']/p")