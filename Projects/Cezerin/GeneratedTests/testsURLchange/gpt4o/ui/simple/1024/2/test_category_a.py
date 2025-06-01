import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class UITestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:3000/category-a")

    def test_ui_elements_presence(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header logo
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "logo-image")))
        except:
            self.fail("Logo element is missing or not visible.")

        # Check search input
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-input")))
        except:
            self.fail("Search input is missing or not visible.")

        # Check cart button
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "cart-button")))
        except:
            self.fail("Cart button is missing or not visible.")

        # Check category title
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "category-title")))
        except:
            self.fail("Category title is missing or not visible.")

        # Check product items
        product_selectors = [
            (By.LINK_TEXT, "Product A"),
            (By.LINK_TEXT, "Product B")
        ]
        for selector in product_selectors:
            try:
                wait.until(EC.visibility_of_element_located(selector))
            except:
                self.fail(f"Product element with selector {selector} is missing or not visible.")

        # Check footer
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer-logo")))
        except:
            self.fail("Footer logo is missing or not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()