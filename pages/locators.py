from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_EMAIL_LINK = (By.CSS_SELECTOR, "[name='login-username']")
    LOGIN_PASSWORD_LINK = (By.CSS_SELECTOR, "[name='login-password']")
    REGISTRATION_EMAIL_LINK = (By.CSS_SELECTOR, "[name='registration-email']")
    REGISTRATION_PASSWORD_LINK = (By.CSS_SELECTOR, "[name='registration-password1']")
    REGISTRATION_REPEAT_PASSWORD_LINK = (By.CSS_SELECTOR, "[name='registration-password2']")

class ProductPageLocators():
    PRODUCT_ADD_TO_BASKET = (By.CSS_SELECTOR, "[class='btn btn-lg btn-primary btn-add-to-basket']")
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, "[class='col-sm-6 product_main'] [class='price_color']")
    PRICE_OF_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "[class='alertinner '] p strong")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, "[class='col-sm-6 product_main'] h1")
    NAME_OF_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "[class='alertinner '] strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "[class='alertinner ']")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
