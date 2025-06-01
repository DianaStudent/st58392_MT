from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium.webdriver.chrome.service import Service as ChromeService

class TestArtPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/9-art")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_presence(self):
        driver = self.driver
        wait = self.wait

        # Verify header and footer
        try:
            wait.until(EC.visibility_of_element_located((By.ID, "header")))
            wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        except:
            self.fail("Header or Footer is missing")

        # Verify navigation
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "nav.header-nav")))
        except:
            self.fail("Navigation bar is missing")

        # Verify product list presence
        try:
            wait.until(EC.visibility_of_element_located((By.ID, "js-product-list")))
        except:
            self.fail("Product list is missing")

        # Verify search input field
        try:
            wait.until(EC.visibility_of_element_located((By.NAME, "s")))
        except:
            self.fail("Search input is missing")

        # Verify key buttons
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(@class,'wishlist-button-add')]")))
        except:
            self.fail("Wishlist add button is missing")

        # Verify sign-in link
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art']")))
        except:
            self.fail("Sign in link is missing")

        # Verify footer subscription text input and button
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='email'][placeholder='Your email address']")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='submit'][value='Subscribe']")))
        except:
            self.fail("Newsletter subscription input or button is missing")

        # Click wishlist button as interaction
        try:
            wishlist_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'wishlist-button-add')]")))
            wishlist_button.click()
            # Confirm UI reacts visually (e.g., wishlist toast appears)
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wishlist-toast")))
        except:
            self.fail("Interaction with wishlist button failed or toast not appearing")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()