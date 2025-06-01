import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestClothesPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/3-clothes")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        try:
            # Verify header is present
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
            self.assertTrue(header.is_displayed())
            
            # Verify contact us link is present
            contact_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Contact us")))
            self.assertTrue(contact_link.is_displayed())

            # Verify sign in link is present
            signin_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
            self.assertTrue(signin_link.is_displayed())

            # Verify cart icon is present
            cart_icon = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "i.shopping-cart")))
            self.assertTrue(cart_icon.is_displayed())

            # Verify search input is present
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[aria-label='Search']")))
            self.assertTrue(search_input.is_displayed())

            # Verify product list is present
            product_list = wait.until(EC.visibility_of_element_located((By.ID, "js-product-list")))
            self.assertTrue(product_list.is_displayed())

        except Exception as e:
            self.fail(f"UI element verification failed: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()