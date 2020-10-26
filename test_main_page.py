import time

def test_should_check_bottom_of_adding_product_with_certain_language(browser):
    button = browser.find_element_by_css_selector("[class='btn btn-lg btn-primary btn-add-to-basket']")
    assert button

    time.sleep(10)

