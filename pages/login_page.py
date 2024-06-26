from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Url doesn't contains key word 'login'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Register form is not presented"
    
    def register_new_user(self, email, password):
        form_for_email =  self.browser.find_element(*LoginPageLocators.EMAIL_FOR_REG_FORM)
        form_for_password = self.browser.find_element(*LoginPageLocators.PASSWORD_FOR_REG_FORM)
        form_for_reapeating_password = self.browser.find_element(*LoginPageLocators.REPEATING_PASSWORD_FOR_REG_FORM)
        reg_button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        form_for_email.send_keys(email)
        form_for_password.send_keys(password)
        form_for_reapeating_password.send_keys(password)
        reg_button.click()