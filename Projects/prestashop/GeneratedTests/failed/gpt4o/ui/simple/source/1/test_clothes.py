from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestClothesPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/3-clothes")

    def test_ui_elements(self):
        driver = self.driver

        try:
            # Check main header
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "header"))
            )

            # Check navigation links
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Contact us"))
            )

            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Sign in"))
            )

            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Cart"))
            )

            # Check breadcrumb
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "breadcrumb"))
            )

            # Check subcategories
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "subcategories-list"))
            )

            # Check products list
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "js-product-list"))
            )

            # Check newsletter subscription
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "submitNewsletter"))
            )

        except Exception as e:
            self.fail(f"UI Element not found: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()