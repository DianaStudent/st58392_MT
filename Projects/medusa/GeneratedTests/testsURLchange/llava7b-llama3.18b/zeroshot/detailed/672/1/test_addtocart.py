import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def test_add_to_cart(self):
        # 1. Open home page
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "menu-button"))
        )
        
        # 2. Click the menu button ("Menu")
        self.driver.find_element(By.ID, "menu-button").click()
        
        # 3. Click the "Store" link
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Store"))
        )
        self.driver.find_element(By.LINK_TEXT, "Store").click()

        # 4. Click on a product image (Thumbnail) - first product
        product_image = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "product-image-0"))
        )
        product_image.click()
        
        # 5. Select size by clicking the size button "L"
        select_size_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[@data-testid='size-button-L']"))
        )
        select_size_button.click()

        # 6. Add the product to the cart
        add_to_cart_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "add-to-cart-button-0"))
        )
        add_to_cart_button.click()

        # 7. Explicitly click the cart button to open the cart
        cart_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[@data-testid='cart-button']"))
        )
        cart_button.click()
        
        # Wait for presence of "GO TO CHECKOUT" button using html_data
        checkout_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "checkout-button"))
        )

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()