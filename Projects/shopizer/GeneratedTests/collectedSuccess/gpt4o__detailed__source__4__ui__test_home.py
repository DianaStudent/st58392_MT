import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestWebsiteUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check header
        header = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "header-area"))
        )
        self.assertIsNotNone(header, "Header is missing")

        # Check footer
        footer = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "footer-area"))
        )
        self.assertIsNotNone(footer, "Footer is missing")

        # Check navigation links
        nav_links = ["Home", "Tables", "Chairs"]
        for link_text in nav_links:
            link = self.wait.until(
                EC.visibility_of_element_located((By.LINK_TEXT, link_text))
            )
            self.assertIsNotNone(link, f"{link_text} link is missing")

        # Check product section
        product_section = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "product-area"))
        )
        self.assertIsNotNone(product_section, "Product section is missing")

        # Check presence of buttons
        buttons = [
            {"selector": (By.ID, "rcc-confirm-button"), "name": "Accept Cookies"},
            {"selector": (By.CLASS_NAME, "account-setting-active"), "name": "Account Menu"},
            {"selector": (By.CLASS_NAME, "icon-cart"), "name": "Cart"},
            {"selector": (By.CLASS_NAME, "button"), "name": "Subscribe"}
        ]
        for button in buttons:
            element = self.wait.until(
                EC.visibility_of_element_located(button["selector"])
            )
            self.assertIsNotNone(element, f"{button['name']} button is missing")

        # Interact with cookie consent button
        cookie_button = driver.find_element(By.ID, "rcc-confirm-button")
        cookie_button.click()

        # Assert page elements after interaction
        # Example: Check Cart reacts
        cart_count = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "count-style"))
        )
        self.assertEqual(cart_count.text, "0", "Cart count text is incorrect")

        # Check form fields
        form_fields = [
            {"selector": (By.NAME, "email"), "name": "Email Input"},
        ]
        for field in form_fields:
            element = self.wait.until(
                EC.visibility_of_element_located(field["selector"])
            )
            self.assertIsNotNone(element, f"{field['name']} is missing")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()