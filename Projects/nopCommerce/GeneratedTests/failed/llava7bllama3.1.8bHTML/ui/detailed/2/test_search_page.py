from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestMaxWebsite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")

    def test_max_website(self):
        # Check structural elements
        header = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "header")))
        footer = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "footer")))

        # Check presence and visibility of input fields, buttons, labels, and sections
        nav_links = self.driver.find_elements(By.CSS_SELECTOR, "nav a")
        search_input = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "search")))
        subscribe_button = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "newsletter-subscribe-button")))

        # Interact with key UI elements
        for link in nav_links:
            if link.text == "Search":
                link.click()

        search_results = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".result")))
        self.assertGreater(len(search_results), 0)

        # Confirm that the UI reacts visually
        subscribe_button.click()
        newsletter_result = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "newsletter-result-block")))

    def test_max_website_navigation(self):
        # Test navigation
        login_link = self.driver.find_element(By.LINK_TEXT, "Login")
        register_link = self.driver.find_element(By.LINK_TEXT, "Register")

        # Click on links
        login_link.click()
        register_link.click()

        # Check if we are on the correct pages
        self.assertEqual(self.driver.current_url, "http://max/login?returnUrl=%2F")
        self.assertEqual(self.driver.current_url, "http://max/register?returnUrl=%2F")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()