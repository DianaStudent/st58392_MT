import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestWebsiteUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/3-clothes")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except:
            self.fail("Header not found or not visible")

        # Check 'Contact us' link
        try:
            contact_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Contact us")))
        except:
            self.fail("'Contact us' link not found or not visible")

        # Check language selector
        try:
            language_selector = wait.until(EC.visibility_of_element_located((By.ID, "_desktop_language_selector")))
        except:
            self.fail("Language selector not found or not visible")

        # Check 'Sign in' link
        try:
            sign_in_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
        except:
            self.fail("'Sign in' link not found or not visible")

        # Check cart widget
        try:
            cart = wait.until(EC.visibility_of_element_located((By.ID, "_desktop_cart")))
        except:
            self.fail("Cart widget not found or not visible")

        # Check category title
        try:
            category_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.h1")))
            self.assertEqual(category_title.text, "Clothes")
        except:
            self.fail("Category title 'Clothes' not found or not visible")

        # Check search bar
        try:
            search_bar = wait.until(EC.visibility_of_element_located((By.NAME, "s")))
        except:
            self.fail("Search bar not found or not visible")

        # Check main products section
        try:
            products_section = wait.until(EC.visibility_of_element_located((By.ID, "products")))
        except:
            self.fail("Main products section not found or not visible")

        # Check footer
        try:
            footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        except:
            self.fail("Footer not found or not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()