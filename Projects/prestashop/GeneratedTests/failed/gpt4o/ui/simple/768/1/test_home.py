from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DemoUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://localhost:8080/en/")

    def test_ui_elements(self):
        driver = self.driver

        try:
            # Verify header and navigation elements
            header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
            self.assertIsNotNone(header, "Header is not visible")

            nav_bar = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-nav")))
            self.assertIsNotNone(nav_bar, "Navigation bar is not visible")

            # Verify top menu links
            clothes_link = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/en/3-clothes']")))
            self.assertIsNotNone(clothes_link, "Clothes category link is not visible")

            accessories_link = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/en/6-accessories']")))
            self.assertIsNotNone(accessories_link, "Accessories category link is not visible")

            art_link = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/en/9-art']")))
            self.assertIsNotNone(art_link, "Art category link is not visible")

            # Verify user options
            sign_in_link = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F']")))
            self.assertIsNotNone(sign_in_link, "Sign in link is not visible")

            register_link = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/en/registration']")))
            self.assertIsNotNone(register_link, "Register link is not visible")

            # Verify search bar functionality
            search_widget = self.wait.until(EC.visibility_of_element_located((By.ID, "search_widget")))
            self.assertIsNotNone(search_widget, "Search widget is not visible")

            search_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Search our catalog']")))
            self.assertIsNotNone(search_input, "Search input is not visible")

            # Verify featured products section
            featured_products = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "featured-products")))
            self.assertIsNotNone(featured_products, "Featured products section is not visible")

        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()