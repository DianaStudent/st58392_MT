from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestMax(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")

    def tearDown(self):
        self.driver.quit()

    def test_main_ui_components(self):
        # Check that the main UI components are present
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "header"))
        )
        
        # Header elements should be visible
        header = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "header > h1"))
        )
        self.assertTrue(header.is_displayed())
        
        # Check that the search bar is present and visible
        search_bar = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, "search-bar"))
        )
        self.assertTrue(search_bar.is_displayed())
        
        # Check that the login link is present and visible
        login_link = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Login"))
        )
        self.assertTrue(login_link.is_displayed())

    def test_login_page(self):
        # Click on the login link
        login_link = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
        ).click()

        # Check that the login page URL is correct
        self.assertEqual(self.driver.current_url, "http://max/login?returnUrl=%2F")

    def test_register_page(self):
        # Click on the register link
        register_link = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
        ).click()

        # Check that the register page URL is correct
        self.assertEqual(self.driver.current_url, "http://max/register?returnUrl=%2F")

    def test_search_page(self):
        # Click on the search button
        search_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "search-button"))
        ).click()

        # Check that the search page URL is correct
        self.assertEqual(self.driver.current_url, "http://max/search")

if __name__ == "__main__":
    unittest.main()