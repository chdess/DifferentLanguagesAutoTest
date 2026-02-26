from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import time


def test_visibility_of_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    try:
        basket_button = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(@class, 'btn-add-to-basket1')]"))
        )
        basket_button_is_visible = True
    except TimeoutException:
        basket_button_is_visible = False

    assert basket_button_is_visible, "Button 'Add to basket' not presented"