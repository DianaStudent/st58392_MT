from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from unittest.mock import MagicMock, patch
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import service_file_path

class TestLoginFunction(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.headless = False
        driver_service = webdriver.Chrome(service=service_file_path)
        self.driver = webdriver.Chrome(options=options, service=driver_service)

    def tearDown(self):
        self.driver.quit()

    def test_login_function(self):
        self.driver.get("http://localhost/")
        
        account_icon = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/login')]")))
        account_icon.click()
        
        login_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'login)]"))