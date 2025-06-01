import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # 1. Open home page.
        category_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a']")))
        if not category_link:
            self.fail("Category link not found on home page")
        category_link.click()

        # 2. Click on product category.
        product_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a/product-a']")))
        if not product_link:
            self.fail("Product link not found on category page")
        product_link.click()

        # 3. Select the first product.
        add_to_cart_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.button-addtocart > button.button"))
        )
        if not add_to_cart_button:
            self.fail("Add to cart button not found on product page")
        add_to_cart_button.click()

        # 4. Click the "Add to cart" button.
        cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.cart-button")))
        if not cart_button:
            self.fail("Cart button not found")
        cart_button.click()

        # 5. Click the cart icon/button to open the shopping bag. 
        go_to_checkout_button = wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/checkout']"))
        )
        if not go_to_checkout_button:
            self.fail("GO TO CHECKOUT button not found inside cart")
        
        # 6. Verify that the "GO TO CHECKOUT" button is present inside the cart.
        go_to_checkout_button.click()

        # 7. Click the "GO TO CHECKOUT" button.
        email_field = wait.until(EC.presence_of_element_located((By.ID, "customer.email")))
        mobile_field = driver.find_element(By.ID, "customer.mobile")
        state_field = driver.find_element(By.ID, "shipping_address.state")
        city_field = driver.find_element(By.ID, "shipping_address.city")

        if not email_field or not mobile_field or not state_field or not city_field:
            self.fail("One or more required checkout fields are missing")

        # 8. Fill out the checkout form using provided credentials.
        email_field.send_keys("mail@mail.com")
        mobile_field.send_keys("12345678")
        state_field.send_keys("Riga")
        city_field.send_keys("Riga")

        # 9. Select a shipping and payment method.
        shipping_method = driver.find_element(By.CSS_SELECTOR, "input[name='shipping_method_id']")
        payment_method = driver.find_element(By.CSS_SELECTOR, "input[name='payment_method_id']")

        if not shipping_method or not payment_method:
            self.fail("Shipping or payment method not found")
        
        shipping_method.click()
        payment_method.click()

        # 10. Click "Next" button.
        next_button = driver.find_element(By.CSS_SELECTOR, "button.checkout-button[type='submit']")
        if not next_button:
            self.fail("Next button not found")
        next_button.click()

        # 11. Click the "Place Order" button.
        place_order_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.checkout-button[type='submit']"))
        )
        if not place_order_button:
            self.fail("Place Order button not found")
        place_order_button.click()

        # 12. Confirm that the success page contains the message: "Thanks for your order!".
        success_message = wait.until(
            EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Thanks for your order!')]"))
        )
        if not success_message:
            self.fail("Success message not found on final page")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()