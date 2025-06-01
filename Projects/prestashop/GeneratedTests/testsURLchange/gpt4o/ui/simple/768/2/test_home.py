import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestKeyUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check if header is present and visible
        header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
        self.assertTrue(header.is_displayed(), "Header is not visible.")

        # Check if navigation links are present and visible
        nav_links = [
            ("Clothes", "http://localhost:8080/en/3-clothes"),
            ("Accessories", "http://localhost:8080/en/6-accessories"),
            ("Art", "http://localhost:8080/en/9-art")
        ]

        for link_text, url in nav_links:
            link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
            self.assertTrue(link.is_displayed(), f"Link '{link_text}' is not visible.")
            self.assertEqual(link.get_attribute('href'), url, f"Link '{link_text}' does not have the expected URL.")

        # Check if login and register links are present and visible
        login_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@title='Log in to your customer account']")))
        self.assertTrue(login_link.is_displayed(), "Login link is not visible.")
        self.assertIn("login", login_link.get_attribute('href'))

        register_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@title='Create account']")))
        self.assertTrue(register_link.is_displayed(), "Register link is not visible.")
        self.assertIn("registration", register_link.get_attribute('href'))

        # Check search input field
        search_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search our catalog']")))
        self.assertTrue(search_input.is_displayed(), "Search input field is not visible.")

        # Check if featured products section is present and visible
        featured_products = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "featured-products")))
        self.assertTrue(featured_products.is_displayed(), "Featured products section is not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()