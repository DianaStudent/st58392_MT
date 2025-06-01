from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_checkout_process(self):
        
        driver = self.driver
        
        # Click on product category
        category_link = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[href='/category-a'")))
        category_link.click()

        # Select the first product
        first_product = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[href='/category-a/product-a']")))
        first_product.click()

        # Click the "Add to cart" button
        add_to_cart_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".button-addtocart button")))
        add_to_cart_button.click()

        # Click the cart icon/button to open the shopping bag
        cart_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-button img[title='cart']")))
        cart_button.click()

        # Verify that the "GO TO CHECKOUT" button is present inside the cart
        go_to_checkout_button = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".mini-cart-open .button.is-primary")
        ))
        if not go_to_checkout_button or not go_to_checkout_button.text.strip():
            self.fail("GO TO CHECKOUT button not found or empty.")

        # Click the "GO TO CHECKOUT" button
        go_to_checkout_button.click()

        # Fill required checkout fields
        email_input = self.wait.until(EC.presence_of_element_located((By.ID, "customer.email")))
        email_input.send_keys("mail@mail.com")
        
        mobile_input = driver.find_element(By.ID, "customer.mobile")
        mobile_input.send_keys("12345678")
        
        country_input = driver.find_element(By.ID, "shipping_address.country")
        if not country_input.get_attribute("value").strip():
            self.fail("Country input is empty.")
        
        state_input = driver.find_element(By.ID, "shipping_address.state")
        state_input.send_keys("Riga")
        
        city_input = driver.find_element(By.ID, "shipping_address.city")
        city_input.send_keys("Riga")

        # Select a shipping and payment method
        shipping_method = driver.find_element(By.CSS_SELECTOR, ".shipping-methods input[type='radio']")
        payment_method = driver.find_element(By.CSS_SELECTOR, ".payment-methods input[type='radio']")
        shipping_method.click()
        payment_method.click()

        # Click "Next" and then "Place Order" to complete the process
        next_button = driver.find_element(By.CSS_SELECTOR, ".checkout-button-wrap .checkout-button")
        next_button.click()

        place_order_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout-step button.is-primary")))
        place_order_button.click()

        # Confirm that the success page contains the message: "Thanks for your order!"
        success_title = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout-success-title")))
        if "Thanks for your order!" not in success_title.text:
            self.fail("Order confirmation message not found or incorrect.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()