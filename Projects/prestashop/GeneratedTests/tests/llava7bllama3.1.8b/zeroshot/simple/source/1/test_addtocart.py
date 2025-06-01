from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager

class TestAddToCart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")

    def test_add_to_cart(self):
        # Add to Cart Button Locator
        add_to_cart_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-name='Add to cart']"))
        )
        
        # Wait for Modal Confirmation
        modal_title = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h4[contains(text(), 'successfully added') or contains(text(), 'added')]"))
        )

        add_to_cart_button.click()
        
        self.assertEqual(modal_title.text.strip(), "Successfully added to cart")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()