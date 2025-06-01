from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class AccessoryPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://localhost:8080/en/6-accessories")

    def test_ui_elements(self):
        driver = self.driver

        # Header elements
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "_desktop_logo")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "search_widget")))
        except:
            self.fail("Header elements are not visible.")

        # Navigation elements
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "top-menu")))
        except:
            self.fail("Navigation elements are not visible.")

        # Main content elements
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "js-product-list")))
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.h1")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "subcategories")))
        except:
            self.fail("Main content elements are not visible.")

        # Footer elements
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "footer")))
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "block_newsletter")))
        except:
            self.fail("Footer elements are not visible.")

        # Interaction: Click on a product
        try:
            product_link = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Mug The adventure begins"))
            )
            product_link.click()
        except:
            self.fail("Product link is not clickable.")

        # Verify the product page loads
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "main")))
        except:
            self.fail("Unable to navigate to the product page.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()