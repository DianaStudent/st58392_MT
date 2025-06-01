import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestCheckout(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")

    def test_checkout_process(self):
        # Open home page.
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

        # Click on product category.
        category_button = self.driver.find_element(By.CSS_SELECTOR, "a[href='/products']")
        category_button.click()

        # Select the first product.
        product_name = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='product-name']")))
        product_name.click()

        # Click the "Add to cart" button.
        add_to_cart_button = self.driver.find_elements(By.CSS_SELECTOR, ".add-to-cart")[0]
        add_to_cart_button.click()

        # Click the cart icon/button to open the shopping bag. 
        cart_icon = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-button")))
        cart_icon.click()

        # Verify that the "GO TO CHECKOUT" button is present inside the cart.
        checkout_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@class='checkout-button']")))
        self.assertTrue(checkout_button.is_enabled())

        # Click the "GO TO CHECKOUT" button.
        checkout_button.click()

        # Fill required checkout fields
        email_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'email')))
        email_field.send_keys("test@example.com")
        
        phone_number_field = self.driver.find_element(By.ID, "phone")
        phone_number_field.send_keys("+1234567890")

        # Select a shipping and payment method.
        shipping_method = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='shipping']")))
        shipping_method.click()

        payment_method = self.driver.find_elements(By.CSS_SELECTOR, "input[name='payment'][value='credit_card']")[0]
        payment_method.click()

        # Click "Next" and then "Place Order" to complete the process.
        next_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@class='next-button']")))
        next_button.click()
        
        place_order_button = self.driver.find_elements(By.CSS_SELECTOR, "button[type='submit']")[1]
        place_order_button.click()

        # Confirm that the success page contains the message: "Thanks for your order!".
        success_message = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h2[text()='Thanks for your order!']")))
        self.assertTrue(success_message.text == 'Thanks for your order!')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()