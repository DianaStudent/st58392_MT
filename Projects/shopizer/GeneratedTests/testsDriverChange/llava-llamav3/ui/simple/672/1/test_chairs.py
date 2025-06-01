```
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class TestSeleniumWebpage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver')
        self.driver.implicitly_wait(20, time_out='300000')

    def tearDown(self):
        self.driver.quit()

    def test_main_ui(self):
        driver = self.driver
        main_ui = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,'//header[contains(text())]')))
        headers = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,'//h1[contains(text())]'))))

    def test_tables(self):
        driver = self.driver
        tables = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,'//div[contains(@class(),"container")]'))
        table_headers = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,'//thead[contains(@role="table-header)]')))
```