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
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_presence(self):
        try:
            # Check header
            self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
            
            # Check main section
            self.wait.until(EC.visibility_of_element_located((By.ID, "main")))
            
            # Check breadcrumb
            breadcrumb = self.driver.find_element(By.CLASS_NAME, "breadcrumb")
            self.assertTrue(breadcrumb.is_displayed(), "Breadcrumb is not visible.")

            # Check filter section
            self.wait.until(EC.visibility_of_element_located((By.ID, "search_filters_wrapper")))
            
            # Check product list
            product_list = self.driver.find_element(By.ID, "products")
            self.assertTrue(product_list.is_displayed(), "Product list is not visible.")

            # Check footer
            self.wait.until(EC.visibility_of_element_located((By.ID, "footer")))

            # Check login link
            login_link = self.driver.find_element(By.CSS_SELECTOR, "[title='Log in to your customer account']")
            self.assertTrue(login_link.is_displayed(), "Login link is not visible.")

            # Check register link
            register_link = self.driver.find_element(By.LINK_TEXT, "Create account")
            self.assertTrue(register_link.is_displayed(), "Register link is not visible.")
            
            # Check cart icon
            cart = self.driver.find_element(By.CSS_SELECTOR, "i.shopping-cart")
            self.assertTrue(cart.is_displayed(), "Cart icon is not visible.")

            # Check product images
            product_images = self.driver.find_elements(By.CSS_SELECTOR, ".product-thumbnail img")
            self.assertGreater(len(product_images), 0, "No product images are visible.")

            # Check search input
            search_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='s']")
            self.assertTrue(search_input.is_displayed(), "Search input is not visible.")

        except Exception as e:
            self.fail(f"Test failed due to missing elements: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()