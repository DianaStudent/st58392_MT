import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestArtPageUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/9-art")

    def test_key_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header elements
        try:
            language_selector = wait.until(EC.visibility_of_element_located((By.ID, "_desktop_language_selector")))
            user_info = driver.find_element(By.ID, "_desktop_user_info")
            user_cart = driver.find_element(By.ID, "_desktop_cart")
        except:
            self.fail("Header elements are missing or not visible.")

        # Check main menu links
        try:
            clothes_link = driver.find_element(By.LINK_TEXT, "Clothes")
            accessories_link = driver.find_element(By.LINK_TEXT, "Accessories")
            art_link = driver.find_element(By.LINK_TEXT, "Art")
        except:
            self.fail("Main menu links are missing or not visible.")

        # Check product list header
        try:
            product_list_header = driver.find_element(By.CSS_SELECTOR, "div.block-category.card.card-block h1.h1")
            self.assertEqual(product_list_header.text, "Art")
        except:
            self.fail("Product list header is missing or not visible.")

        # Check products presence
        try:
            product_elements = driver.find_elements(By.CSS_SELECTOR, "div.js-product.product")
            if len(product_elements) < 1:
                self.fail("Product elements are missing or not visible.")
        except:
            self.fail("Product elements are missing or not visible.")
        
        # Check sign in link
        try:
            sign_in_link = driver.find_element(By.LINK_TEXT, "Sign in")
        except:
            self.fail("Sign in link is missing or not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()