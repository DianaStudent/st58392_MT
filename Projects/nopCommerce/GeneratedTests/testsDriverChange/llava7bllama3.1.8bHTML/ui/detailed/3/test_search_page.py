import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService

class TestMaxWebsite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        # 1. Load the page and ensure that structural elements are visible
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "header")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "footer")))

        # 2. Check the presence and visibility of input fields, buttons, labels, and sections
        elements = [
            ("login-email", By.NAME, "email"),
            ("register-email", By.NAME, "email"),
            ("search-field", By.NAME, "q"),
            ("newsletter-subscribe-button", By.XPATH, "//button[@id='newsletter-subscribe-button']"),
            ("header-links", By.TAG_NAME, "ul"),
            ("footer-links", By.TAG_NAME, "ul")
        ]
        for element_name, locator_type, locator_value in elements:
            try:
                WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((locator_type, locator_value)))
            except TimeoutException:
                self.fail(f"Missing required UI element: {element_name}")

        # 3. Interact with key UI elements (e.g., click buttons)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='login-button']"))).click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "register-email")))

    def test_ui_reacts_visually(self):
        # Interact with UI elements and confirm visual changes
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='search-button']"))).click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "search-results")))
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "search-results"))))

if __name__ == "__main__":
    unittest.main()