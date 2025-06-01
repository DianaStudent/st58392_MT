from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestMaxHomePage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")

    def test_home_page_elements(self):
        # Navigation links
        nav_links = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".nav-link"))
        )
        self.assertEqual(len(nav_links), 4)
        for link in nav_links:
            self.assertTrue(link.is_displayed())

        # Inputs and buttons
        search_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "search-input"))
        )
        self.assertTrue(search_input.is_displayed())
        submit_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#submit-button"))
        )
        self.assertTrue(submit_button.is_displayed())

        # Banners
        banner = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "banner"))
        )
        self.assertTrue(banner.is_displayed())

    def test_interact_with_elements(self):
        submit_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#submit-button"))
        )
        submit_button.click()
        # Check that UI updates visually
        search_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "search-input"))
        )
        self.assertTrue(search_input.is_displayed())

    def test_no_errors_on_interactive_elements(self):
        nav_links = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".nav-link"))
        )
        for link in nav_links:
            link.click()
            # Check that UI does not throw an error
            self.assertTrue(self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()