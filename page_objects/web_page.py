from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


class AccessWebPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = "https://www.startpage.com/"

#Elementos:

        self.input_search = (By.ID, "q")
        self.btn_search = (By.CLASS_NAME, "search-btn")
        self.result_search = (By.XPATH, "//*[@id='e1']/div/div/div[3]/a")


    def open_webpage(self):
            self.driver.get(self.base_url)


    def search_qa(self, word: str):
        self.wait.until(EC.visibility_of_element_located(self.input_search)).send_keys(word)
        search_button = self.wait.until(EC.element_to_be_clickable(self.btn_search))
        search_button.send_keys(Keys.ENTER)


    def result(self):
        self.wait.until(EC.visibility_of_element_located(self.result_search)).click()