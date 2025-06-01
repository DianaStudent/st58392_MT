from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestEcommerceWebsite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver = driver

    def tearDown(self):
        self.driver.quit()

    def test_1_open_page(self):
        self.driver.get("http://localhost:8080/en/")

    def test_2_verify_ui_elements(self):
        assert self.driver.find_element_by_css_selector(".nav-link")
        assert self.driver.find_element_by_name("searchbar")
        assert self.driver.find_element_by_tag_name("form")

    def test_3_interact_with_button(self):
        time.sleep(2)  # add delay before interacting with button
        self.driver.find_element_by_css_selector(".btn-primary").click()
        time.sleep(5)
        self.assertEqual(self.driver.title, "Shopping Cart - Ecommerce Website")