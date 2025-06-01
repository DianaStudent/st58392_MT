from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestArtPage(unittest.TestCase):

    def setUp(self):
        # Set up ChromeDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_art_page_ui(self):
        driver = self.driver
        driver.get("http://localhost:8080/en/9-art")

        # Define a wait object with a timeout of 20 seconds
        wait = WebDriverWait(driver, 20)

        # Check visibility of header
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except:
            self.fail("Header not found or not visible.")

        # Check visibility of footer
        try:
            footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        except:
            self.fail("Footer not found or not visible.")

        # Check visibility of main menu links
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="http://localhost:8080/en/3-clothes"]')))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="http://localhost:8080/en/6-accessories"]')))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="http://localhost:8080/en/9-art"]')))
        except:
            self.fail("Main menu links not found or not visible.")

        # Check visibility of sign-in link
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art"]')))
        except:
            self.fail("Sign-in link not found or not visible.")

        # Check visibility of products
        try:
            products_section = wait.until(EC.visibility_of_element_located((By.ID, "products")))
            products = products_section.find_elements(By.CLASS_NAME, "product-miniature")
            self.assertTrue(len(products) > 0, "Products not found or not visible.")
        except:
            self.fail("Products section not found or not visible.")

        # Check visibility of search input
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[aria-label="Search"]')))
        except:
            self.fail("Search input not found or not visible.")

        # Interact with wishlist button
        try:
            wishlist_buttons = driver.find_elements(By.CSS_SELECTOR, 'button.wishlist-button-add')
            if wishlist_buttons:
                wishlist_buttons[0].click()
        except:
            self.fail("Wishlist button interaction failed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()