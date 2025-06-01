from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager

class TestMaxSite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def tearDown(self):
        self.driver.quit()

    def test_max_site_structure(self):
        # Load the page
        self.driver.get("http://max/")

        # Check structural elements (header, footer, navigation)
        header = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#header")))
        self.assertTrue(header.is_displayed())

        footer = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#footer")))
        self.assertTrue(footer.is_displayed())

        nav_links = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".nav-link")))
        for link in nav_links:
            self.assertTrue(link.is_displayed())

        # Check input fields and buttons
        email_input = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.NAME, "email")))
        password_input = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.NAME, "password")))

        subscribe_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#newsletter-subscribe-button")))
        self.assertTrue(subscribe_button.is_displayed())

        # Interact with key UI elements (click button)
        subscribe_button.click()

        # Confirm that the UI reacts visually
        email_input.send_keys("test@example.com")
        password_input.send_keys("password")

        # Assert that no required UI element is missing
        self.assertTrue(len(nav_links) > 0)

if __name__ == "__main__":
    unittest.main()