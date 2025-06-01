from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestAccessoriesPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/6-accessories")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        try:
            # Header UI Components
            self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-nav")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "category")))

            # Navigation links
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/3-clothes']")))
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/6-accessories']")))
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/9-art']")))

            # Sign in link
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F6-accessories']")))

            # Main content
            self.wait.until(EC.visibility_of_element_located((By.ID, "content-wrapper")))
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.h1")))

            # Products
            products = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "js-product")))
            self.assertFalse(len(products) == 0, "No products found on the page")

        except Exception as e:
            self.fail(f"Test failed due to missing element: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()