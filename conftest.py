import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en-gb",
                     help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    browser = webdriver.Chrome()
    browser.get(link)
    yield browser
    browser.quit()
