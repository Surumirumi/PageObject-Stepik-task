from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.product_page import ProductPage
import time
import pytest

@pytest.mark.parametrize('promo_offer', ["0","1", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail(reason="won't be wixed")), "8", "9"])
def  test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.add_item_to_busket()
    product_page.solve_quizes_and_get_code()
    product_page.should_be_product_in_basket()
