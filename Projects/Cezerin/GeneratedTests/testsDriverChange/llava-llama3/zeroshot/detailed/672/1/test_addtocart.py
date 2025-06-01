import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

class TestAddToCartProcess(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_addtocart_process(self):
        # Step 1: Open home page
        self.driver.get("http://localhost:3000/")
        
        # Step 2: Click on product category
        category_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'CATEGORY A')]")))
        category_button.click()
        
        # Step 3: Select the first product
        product_card = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'PRODUCT A')]}")))
        product_card.click()
        
        # Step 4: Click the "ADD TO CART" button
        addtocart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'ADD TO CART')]")))
        addtocart_button.click()

        # Step 5: Open the mini-cart by clicking on the cart icon
        cart_icon = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'SHOPPING BAG']}")))
        cart_icon.click()
        
        # Verify that the "GO TO CHECKOUT" button is present in the cart
        go_to_checkout_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'PROCEED TO CHECKOUT')]")))
        self.assertTrue(expected_conditions.presence_of_element_located((By.XPATH, "//button[contains(text(), 'PROCEED TO CHECKOUT']}"))))

if __name__ == "__main__":
    unittest.main()