import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class UITestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check header
        header = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'header.header-area')))
        self.assertIsNotNone(header, "Header is not visible")

        # Check footer
        footer = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'footer.footer-area')))
        self.assertIsNotNone(footer, "Footer is not visible")

        # Check navigation links
        nav_links = ['Home', 'Tables', 'Chairs']
        for link_text in nav_links:
            link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
            self.assertIsNotNone(link, f"Navigation link '{link_text}' is not visible")

        # Check buttons and inputs
        try:
            accept_cookies_button = self.wait.until(EC.visibility_of_element_located((By.ID, 'rcc-confirm-button')))
            self.assertIsNotNone(accept_cookies_button, "Accept cookies button is not visible")
            accept_cookies_button.click()

            subscribe_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.subscribe-form button.button')))
            self.assertIsNotNone(subscribe_button, "Subscribe button is not visible")

            email_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type="email"]')))
            self.assertIsNotNone(email_input, "Email input field is not visible")

        except Exception as e:
            self.fail(f"UI element interaction failed: {e}")

        # Check product section
        product_section = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.product-area')))
        self.assertIsNotNone(product_section, "Product section is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()