import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class MedusaStoreTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart_process(self):
        driver = self.driver

        # 1. Open home page - already done in setUp()

        # 2. Click on the menu button
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']"))).click()

        # 3. Click on the "Store" link
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='store-link']"))).click()

        # 4. Click on a product image (thumbnail)
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul[data-testid='products-list'] li a"))).click()

        # 5. Select a size
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='L']"))).click()

        # 6. Click the "Add to Cart" button
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-product-button']"))).click()

        # 7. Click the cart button to open the cart
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-cart-link']"))).click()

        # 8. Verify that the "GO TO CHECKOUT" button is present
        checkout_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='go-to-cart-button']")))
        
        # Assert the "GO TO CHECKOUT" button is present and not empty
        if not checkout_button:
            self.fail("Checkout button is not present")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()