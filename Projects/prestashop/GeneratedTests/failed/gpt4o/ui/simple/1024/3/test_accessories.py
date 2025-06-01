from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class AccessoriesPageUITest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/6-accessories")
    
    def test_page_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Verify the header is visible
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
            
            # Verify presence of 'Accessories' page title
            page_title = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "title")))
            self.assertIn("Accessories", driver.title)

            # Verify the main title on the page
            main_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.h1")))
            self.assertIn("Accessories", main_title.text)

            # Verify the navigation bar links
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            clothing_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            accessories_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            art_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))

            # Verify the 'Sign in' link
            sign_in_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
            
            # Verify the search bar is visible
            search_bar = wait.until(EC.visibility_of_element_located((By.NAME, "s")))

            # Verify product listings are visible
            product_listings = wait.until(EC.visibility_of_element_located((By.ID, "js-product-list")))

        except Exception as e:
            self.fail(f"UI component missing or not visible: {str(e)}")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()