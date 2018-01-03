from pypom import Page
from selenium import webdriver


def test_is_loaded():
    driver = webdriver.Firefox()
    driver.get('http://mozilla.org')
    page = Page(driver)
    assert page.is_loaded is True
    driver.close()


def test_is_loaded_when_no_url_is_present():
    driver = webdriver.Firefox()
    page = Page(driver)
    assert page.is_loaded is True
    driver.close()
