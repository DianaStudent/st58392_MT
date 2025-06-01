import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestPageElements(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.get("http://localhost:8080/en/6-accessories")
        cls.wait = WebDriverWait(cls.driver, 20)

    def test_main_ui_elements(self):
        try:
            # Check header
            header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
            
            # Check main title
            main_title = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.h1")))
            
            # Check product list
            product_list = self.wait.until(EC.visibility_of_element_located((By.ID, "js-product-list")))
            
            # Check language selector
            language_selector = self.wait.until(EC.visibility_of_element_located((By.ID, "_desktop_language_selector")))
            
            # Check login link
            login_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F6-accessories']")))
            
            # Check cart
            cart = self.wait.until(EC.visibility_of_element_located((By.ID, "_desktop_cart")))
            
            # Check product items
            product_items = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".js-product")))

        except Exception as e:
            self.fail(f"UI element not found or not visible: {e}")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()