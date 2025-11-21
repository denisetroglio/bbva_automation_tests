from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class WebPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.cookies = (By.ID, "W0wltc") 
        self.url = ""

    def configure_website(self, website):
        if website == "Google":
            self.url = "https://www.google.com/"
            self.input_search = (By.ID, "APjFqb")
            self.result_search = (By.CSS_SELECTOR, "h3")
        else:
            self.url = "https://duckduckgo.com/"
            self.input_search = (By.ID, "searchbox_input")
            self.result_search = (By.CSS_SELECTOR, "a[data-testid='result-title-a']")

    def visit(self, url: str):
        self.driver.get(url)
        try:
            self.wait.until(EC.element_to_be_clickable(self.cookies)).click()
        except:
            pass

    def search_by(self, word: str):
        search_box = self.wait.until(
            EC.visibility_of_element_located(self.input_search)
        )
        search_box.send_keys(word + Keys.RETURN)

    def click_on_first_result(self):
        first_result = self.wait.until(
            EC.element_to_be_clickable(self.result_search)
        )
        first_result.click()
