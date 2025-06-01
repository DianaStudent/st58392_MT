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
        wait = WebDriverWait(driver, 20)

        # Check for header visibility
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except:
            self.fail("Header is not visible")

        # Check for footer visibility
        try:
            footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        except:
            self.fail("Footer is not visible")

        # Check for main navigation links
        for link_text in ["Clothes", "Accessories", "Art"]:
            try:
                nav_link = wait.until(
                    EC.visibility_of_element_located((By.LINK_TEXT, link_text))
                )
            except:
                self.fail(f"Navigation link '{link_text}' is not visible")

        # Check for login link
        try:
            login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
        except:
            self.fail("Login link is not visible")

        # Check for search input
        try:
            search_input = wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[aria-label="Search"]'))
            )
        except:
            self.fail("Search input is not visible")

        # Check for newsletter subscription
        try:
            newsletter_input = wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type="email"]'))
            )
        except:
            self.fail("Newsletter email input is not visible")

        # Check visibility of products
        product_titles = ["Hummingbird printed t-shirt", "Hummingbird printed sweater"]
        for title in product_titles:
            try:
                product = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, title)))
            except:
                self.fail(f"Product '{title}' is not visible")

        # Check that cart is visible
        try:
            cart = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "cart-preview")))
        except:
            self.fail("Cart is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()