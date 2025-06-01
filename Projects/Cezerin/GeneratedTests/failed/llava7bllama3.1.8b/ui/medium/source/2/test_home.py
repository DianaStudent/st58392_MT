from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestWebsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost:3000')

    def test_navigation_links(self):
        # Wait until navigation links are visible
        navigation_links = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'nav a'))
        )
        
        for link in navigation_links:
            self.failUnless(link.is_displayed())

    def test_button_click(self):
        # Wait until button is visible
        button = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]'))
        )
        
        # Click the button
        button.click()

        # Verify that UI updates visually after clicking the button
        # You can add your own verification steps here, e.g., verify text change

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()