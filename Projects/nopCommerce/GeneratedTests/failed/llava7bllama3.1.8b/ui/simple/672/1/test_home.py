from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class TestNexCommerce(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://max/")

    def test_homepage_elements(self):
        # Check that the main UI components are present: headers, buttons, links, form fields, etc.
        
        # Header
        header = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "header")))
        self.assertIsNotNone(header)

        # Hero Section
        hero_section = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "hero-section")))
        self.assertIsNotNone(hero_section)
        
        # Call-to-Action Button
        call_to_action_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".shop-now-btn")))
        self.assertIsNotNone(call_to_action_button)

        # Social Media Icons
        social_media_icons = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "social-icon")))
        self.assertGreaterEqual(len(social_media_icons), 3)
        
    def test_login_and_register_links(self):
        # Click on the login link to check if it redirects to the login page
        login_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
        login_link.click()
        self.assertEqual(self.driver.current_url, 'http://max/login?returnUrl=%2F')

        # Click on the register link to check if it redirects to the register page
        register_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
        register_link.click()
        self.assertEqual(self.driver.current_url, 'http://max/register?returnUrl=%2F')

    def test_search_box(self):
        # Enter some text into the search box and submit it
        search_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "search")))
        search_input.send_keys("test")
        time.sleep(1)
        
        # Click on the search button to check if it redirects to the search page
        search_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".search-btn")))
        search_button.click()
        self.assertEqual(self.driver.current_url, 'http://max/search')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()