import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class ArtPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/9-art")

    def test_art_page_ui_elements(self):
        driver = self.driver
        
        try:
            # Check Header
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "header"))
            )
            
            # Check Navigation Links
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Home"))
            )
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Clothes"))
            )
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Accessories"))
            )
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Art"))
            )

            # Check Login Link
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Sign in"))
            )
            
            # Check Product Listings
            products = WebDriverWait(driver, 20).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".product-miniature"))
            )
            if not products:
                self.fail("Product listings are not visible.")
            
            # Check Subscription Form
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "email"))
            )
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "submitNewsletter"))
            )
            
        except Exception as e:
            self.fail(f"UI element check failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()