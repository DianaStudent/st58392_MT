from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestWebsite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/en/")

    def tearDown(self):
        self.driver.quit()

    def test_homepage_elements(self):
        # Check that the main UI components are present: headers, buttons, links
        header = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'New Arrivals')]")))
        self.assertTrue(header.is_displayed())

        button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/en/3-clothes')]")))
        self.assertTrue(button.is_displayed())
        self.assertTrue(button.get_attribute("data-toggle") == "modal")

    def test_clothes_elements(self):
        self.driver.get("http://localhost:8080/en/3-clothes")
        header = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Sale')]")))
        self.assertTrue(header.is_displayed())

        button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/en/3-clothes']}"))