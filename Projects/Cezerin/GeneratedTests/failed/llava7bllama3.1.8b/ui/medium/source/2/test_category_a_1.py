from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import unittest

class TestUi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        cls.driver = webdriver.Chrome(options=chrome_options)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_ui_elements(self):
        self.driver.get('http://localhost:3000')

        # Check navigation links are present and visible
        nav_links = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'nav a')))
        for link in nav_links:
            self.assertEqual(link.is_displayed(), True)

        # Check inputs are present and visible
        search_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="search"]')))
        self.assertEqual(search_input.is_displayed(), True)

        # Check buttons are present and visible
        view_all_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-view-all')))
        self.assertEqual(view_all_button.is_displayed(), True)
        add_to_cart_buttons = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.add-to-cart')))
        for button in add_to_cart_buttons:
            self.assertEqual(button.is_displayed(), True)

        # Check banners are present and visible
        banner = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h1.banner')))
        self.assertEqual(banner.is_displayed(), True)

        # Interact with elements
        view_all_button.click()
        add_to_cart_buttons[0].click()

        # Check for UI updates visually
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.updated-ui')))

if __name__ == '__main__':
    unittest.main()