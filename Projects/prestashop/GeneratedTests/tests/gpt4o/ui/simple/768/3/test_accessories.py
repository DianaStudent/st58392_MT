from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time

class AccessoriesPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/6-accessories")
        self.wait = WebDriverWait(self.driver, 20)

    def test_UI_elements_present_and_visible(self):
        driver = self.driver
        
        # Check header elements
        try:
            header_contact = self.wait.until(EC.visibility_of_element_located((By.ID, "contact-link")))
            header_logo = self.wait.until(EC.visibility_of_element_located((By.ID, "_desktop_logo")))
            header_language_selector = self.wait.until(EC.visibility_of_element_located((By.ID, "_desktop_language_selector")))
            header_sign_in = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[title='Log in to your customer account']")))
            
            # Check menu links
            menu_home = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/']")))
            menu_clothes = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/3-clothes']")))
            menu_accessories = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/6-accessories']")))
            menu_art = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/9-art']")))

            # Check subcategory links
            subcategory_stationery = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/7-stationery']")))
            subcategory_home_accessories = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/8-home-accessories']")))

            # Check product elements
            product_elements = self.wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "product-miniature")))
            if len(product_elements) < 11:
                self.fail("Not all products are visible.")

        except Exception as e:
            self.fail(f"Element not found or not visible: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()