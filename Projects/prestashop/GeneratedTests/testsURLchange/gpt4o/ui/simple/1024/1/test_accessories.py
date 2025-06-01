import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestAccessoriesPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/6-accessories")

    def tearDown(self):
        self.driver.quit()

    def test_key_ui_elements_present_and_visible(self):
        driver = self.driver

        try:
            # Check for header elements
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "header")))

            # Check for breadcrumb
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "breadcrumb")))

            # Check for main category content
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))

            # Check for subcategories
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "subcategories-list")))

            # Check if the products element is present and visible
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "js-product-list")))

            # Check for footer elements
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "footer")))

            # Check for search bar
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "search_widget")))
            
            # Check for cart
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "_desktop_cart")))
            
            # Check for login link
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//a[@title='Log in to your customer account']")))

        except Exception as e:
            self.fail(f"Failed to find or verify visibility of required elements: {e}")

if __name__ == '__main__':
    unittest.main()