import pytest_bdd
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from pytest_bdd import scenario, given, when, then
from page_objects.web_page import AccessWebPage 
import logging
import time
import os

logger = logging.getLogger(__name__)

feature_file = os.path.join(os.path.dirname(__file__), "../features/search_qa.feature")


@scenario(feature_file, "Search for the word “QA”")
def test_search_qa():
    pass

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def web_page(driver):
    return AccessWebPage(driver)


@given("the the Google webpage is open")
def access_webpage(web_page):
    web_page.open_webpage()


@when("the user enters QA in the search box")
def search(web_page):
    web_page.search_qa("QA")
    time.sleep(5)


@then("the user click on the first search result")
def clik_result(web_page):
    web_page.result()
