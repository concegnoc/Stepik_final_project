from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "No login part in url"

    def should_be_login_form(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL_LINK)
        self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD_LINK)
        assert True, "No such elements of login form"

    def should_be_register_form(self):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_LINK)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_LINK)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_REPEAT_PASSWORD_LINK)
        assert True, "No such elements of registration form"

    def register_new_user(self, email, password):
        email1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_LINK)
        email1.send_keys(email)
        password1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_LINK)
        password1.send_keys(password)
        password2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_REPEAT_PASSWORD_LINK)
        password2.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON_LINK)
        button.click()
