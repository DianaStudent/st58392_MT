import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestArtPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/9-art")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        
        # Check for headers
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
            self.assertTrue(header.is_displayed())
        except:
            self.fail("Header not present or not visible")

        # Check for navigation links
        try:
            home_link = self.wait.until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Home"))
            )
            self.assertTrue(home_link.is_displayed())

            clothes_link = self.wait.until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Clothes"))
            )
            self.assertTrue(clothes_link.is_displayed())

            accessories_link = self.wait.until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Accessories"))
            )
            self.assertTrue(accessories_link.is_displayed())

            art_link = self.wait.until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Art"))
            )
            self.assertTrue(art_link.is_displayed())
        except:
            self.fail("Navigation links not present or not visible")

        # Check for inputs
        try:
            search_input = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='s']"))
            )
            self.assertTrue(search_input.is_displayed())
        except:
            self.fail("Search input field not present or not visible")

        # Check for buttons
        try:
            subscribe_button = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='submitNewsletter']"))
            )
            self.assertTrue(subscribe_button.is_displayed())
        except:
            self.fail("Subscribe button not present or not visible")

        # Check for banners
        try:
            banner = self.wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "header-banner"))
            )
            self.assertTrue(banner.is_displayed())
        except:
            self.fail("Banner not present or not visible")
        
        # Interact with a button and check UI updates
        try:
            cart_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".wishlist-button-add"))
            )
            cart_button.click()

            # Confirm the interaction - for simplicity, we're checking if the button is still there
            # A real interaction may require page reload, or checking for specific UI updates
            self.assertTrue(cart_button.is_displayed())
        except:
            self.fail("Interacting with cart button failed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()