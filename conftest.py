from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as OptionsFirefox

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: 'en', 'fr', etc..")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")

    options_firefox = OptionsFirefox()
    options_firefox.set_preference("intl.accept_languages", user_language)

    options = Options()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language})

    if browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=options_firefox)

    else: 
        browser = webdriver.Chrome(options=options)
        print("\nstart chrome browser for test..")

    yield browser
    print("\nquit browser..")
    browser.quit()
