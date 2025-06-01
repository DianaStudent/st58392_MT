from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class ArtPageTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/9-art")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Verify header elements
        self.assert_element_visible(By.ID, "header")

        # Verify navigation links
        self.assert_element_visible(By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']")
        self.assert_element_visible(By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']")
        self.assert_element_visible(By.XPATH, "//a[@href='http://localhost:8080/en/9-art']")

        # Verify login link
        self.assert_element_visible(By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art']")

        # Verify registration link
        self.assert_element_visible(By.XPATH, "//a[@href='http://localhost:8080/en/registration']")

        # Verify search input field
        self.assert_element_visible(By.XPATH, "//input[@name='s']")

        # Verify presence of product list
        self.assert_element_visible(By.ID, "products")

        # Click on a product thumbnail and verify the quick view
        product_thumbnail = self.assert_element_visible(By.XPATH, "//a[@href='http://localhost:8080/en/art/3-13-the-best-is-yet-to-come-framed-poster.html#/19-dimension-40x60cm']")
        product_thumbnail.click()

        # Verify that the quick view modal shows up
        self.assert_element_visible(By.CLASS_NAME, "quick-view")

    def assert_element_visible(self, by, value):
        """Helper function to assert element is visible."""
        element = self.wait.until(EC.visibility_of_element_located((by, value)))
        if not element:
            self.fail(f"Element {value} not found or not visible on page.")
        return element

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()