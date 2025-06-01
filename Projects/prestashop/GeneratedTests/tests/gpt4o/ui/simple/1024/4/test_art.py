import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/9-art")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Verify that the header is present and visible
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except:
            self.fail("Header is not visible")

        # Verify that the language selector button is present and visible
        try:
            language_selector = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".language-selector")))
        except:
            self.fail("Language selector is not visible")

        # Verify that the sign-in link is present and visible
        try:
            sign_in_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
        except:
            self.fail("Sign in link is not visible")

        # Verify that the cart icon is present and visible
        try:
            cart = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart")))
        except:
            self.fail("Cart icon is not visible")

        # Verify menu items are present and visible
        menu_items = ["Home", "Clothes", "Accessories", "Art"]
        for item in menu_items:
            try:
                menu_element = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, item)))
            except:
                self.fail(f"Menu item '{item}' is not visible")

        # Verify that the search field is present and visible
        try:
            search_field = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='s']")))
        except:
            self.fail("Search field is not visible")

        # Verify that products are present and visible
        try:
            products = self.wait.until(EC.visibility_of_element_located((By.ID, "products")))
        except:
            self.fail("Products section is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()