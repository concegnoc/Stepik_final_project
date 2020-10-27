from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_EMAIL_LINK = (By.CSS_SELECTOR, "[name='login-username']")
    LOGIN_PASSWORD_LINK = (By.CSS_SELECTOR, "[name='login-password']")
    REGISTRATION_EMAIL_LINK = (By.CSS_SELECTOR, "[name='registration-email']")
    REGISTRATION_PASSWORD_LINK = (By.CSS_SELECTOR, "[name='registration-password1']")
    REGISTRATION_REPEAT_PASSWORD_LINK = (By.CSS_SELECTOR, "[name='registration-password2']")
