import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")

    def test_add_to_cart(self):
        driver = self.driver
        
        try:
            # Wait and click on the 'Art' category
            art_category = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Art')]"))
            )
            art_category.click()

            # Wait and click on the 'The best is yet to come' product
            product = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='http://localhost:8080/en/art/3-13-the-best-is-yet-to-come-framed-poster.html#/19-dimension-40x60cm']"))
            )
            product.click()

            # Wait and click on the 'Add to cart' button
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add to cart')]"))
            )
            add_to_cart_button.click()

            # Wait for the modal to confirm the product was added
            modal_title = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//h4[contains(text(), 'successfully added')]"))
            )
            
            # Check if modal title is present
            self.assertTrue(modal_title.is_displayed())

        except Exception as e:
            self.fail(f'Test failed: {e}')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()