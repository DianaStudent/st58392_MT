import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestArtPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/9-art")

    def test_art_page_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check for navigation links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            clothes_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            accessories_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            art_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))
            login_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[title='Log in to your customer account']")))
            register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Create account")))
        except Exception as e:
            self.fail(f"Failed to find navigation links: {str(e)}")

        # Check for header
        header = driver.find_element(By.TAG_NAME, "header")
        if not header.is_displayed():
            self.fail("Header not visible")

        # Check for search input
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.NAME, "s")))
        except Exception as e:
            self.fail(f"Failed to find search input: {str(e)}")

        # Check for buttons - checking one button example 'Cart'
        try:
            cart_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart")))
        except Exception as e:
            self.fail(f"Failed to find cart button: {str(e)}")

        # Interact with one element - click 'Cart' button and check for UI update
        try:
            cart_button.click()
            cart_dropdown = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart-preview")))
            if not cart_dropdown.is_displayed():
                self.fail("Cart dropdown did not display after clicking cart button")
        except Exception as e:
            self.fail(f"Failed during cart button interaction: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()