import os
import logging
import pytest
from selenium import webdriver
from pytest_bdd import scenario, given, when, then, parsers
from page_objects.web_page import WebPage 

logger = logging.getLogger(__name__)

feature_file = os.path.join(os.path.dirname(__file__), "../features/search_by.feature")
@scenario(feature_file, 'Search by "<word>" and click on first result')
def test_search_by(driver):
    pass

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def web_page(driver):
    return WebPage(driver)

# Step Definitions
@given(parsers.cfparse("the {website} is open"))
def visit_webpage(web_page, website):
    web_page.configure_website(website)
    logger.info(f"Go to: {web_page.url}")
    web_page.visit(web_page.url)

@when(parsers.cfparse("the user enters {word} in the search box"))
def search(web_page, word):
    logger.info(f"Searching by: {word}")
    web_page.search_by(word)

@then('the user click on the first search result')
def click_result(web_page):
    old_url = web_page.driver.current_url
    
    logger.info("Clicking on the first result")
    web_page.click_on_first_result()

    new_url = web_page.driver.current_url
    logger.info(f"New URL: {new_url}")

    assert new_url != old_url, "The first result click did NOT navigate to a new page!"
    assert len(web_page.driver.title) > 0, "The opened page has no title, navigation failed."
