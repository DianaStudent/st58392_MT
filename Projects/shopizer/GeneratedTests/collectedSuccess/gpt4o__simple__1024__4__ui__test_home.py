import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class ShopizerUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_presence(self):
        try:
            # Check header elements
            header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
            self.assertIsNotNone(header, "Header is not present or visible.")

            # Check navigation links
            nav_links = [
                (By.LINK_TEXT, 'Home'),
                (By.LINK_TEXT, 'Tables'),
                (By.LINK_TEXT, 'Chairs'),
            ]
            for selector in nav_links:
                link = self.wait.until(EC.visibility_of_element_located(selector))
                self.assertIsNotNone(link, f"Navigation link {selector[1]} is not present or visible.")

            # Check Cookie Consent button
            cookie_button = self.wait.until(EC.visibility_of_element_located((By.ID, 'rcc-confirm-button')))
            self.assertIsNotNone(cookie_button, "Cookie confirm button is not present or visible.")

            # Check logo
            logo = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.logo img')))
            self.assertIsNotNone(logo, "Logo is not present or visible.")

            # Check footer elements
            footer = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
            self.assertIsNotNone(footer, "Footer is not present or visible.")

            # Check subscription form
            subscribe_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.subscribe-form input[type="email"]')))
            self.assertIsNotNone(subscribe_input, "Subscription input is not present or visible.")

            subscribe_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.subscribe-form button')))
            self.assertIsNotNone(subscribe_button, "Subscription button is not present or visible.")

        except Exception as e:
            self.fail(f"An expected UI element was not found: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()