import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestAddToCartProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver

        # Step 2: Click on a product category
        try:
            category_element = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//ul[@id='top-menu']//a[contains(@href, '9-art')]"))
            )
            category_element.click()
        except Exception as e:
            self.fail(f"Failed to find and click on a product category. Error: {e}")

        # Step 3: Select the first product listed in the category
        try:
            product_element = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'products')]//a[@class='thumbnail product-thumbnail']"))
            )
            product_element.click()
        except Exception as e:
            self.fail(f"Failed to find and click on the first product. Error: {e}")

        # Step 4: On the product detail page, click the "Add to cart" button
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary.add-to-cart"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Failed to find and click the 'Add to cart' button. Error: {e}")

        # Step 5: Wait for the modal popup that confirms the product was added to the cart
        try:
            modal_title = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@id='blockcart-modal']//h4[contains(@class, 'modal-title')]"))
            )
            self.assertIn("Product successfully added to your shopping cart", modal_title.text)
        except Exception as e:
            self.fail(f"Failed to verify the modal confirmation title. Error: {e}")

if __name__ == "__main__":
    unittest.main()