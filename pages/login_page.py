from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "No login part in url"

    def should_be_login_form(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL_LINK)
        self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD_LINK)
        # реализуйте проверку, что есть форма логина
        assert True, "No such elements of login form"

    def should_be_register_form(self):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_LINK)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_LINK)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_REPEAT_PASSWORD_LINK)
        # реализуйте проверку, что есть форма регистрации на странице
        assert True, "No such elements of registration form"