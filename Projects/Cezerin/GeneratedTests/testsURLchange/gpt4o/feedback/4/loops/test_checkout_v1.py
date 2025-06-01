import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:3000/")
        self.driver.maximize_window()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open home page
        driver.get("http://localhost:3000/")

        # Step 2: Click on product category
        category_link = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/category-a"]'))
        )
        self.assertTrue(category_link.is_displayed(), "Category link is not visible.")
        category_link.click()

        # Step 3: Select the first product
        product_link = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/category-a/product-a"]'))
        )
        self.assertTrue(product_link.is_displayed(), "Product link is not visible.")
        product_link.click()

        # Step 4: Click the "Add to cart" button
        add_to_cart_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.button-addtocart button'))
        )
        self.assertTrue(add_to_cart_button.is_displayed(), "Add to cart button is not visible.")
        add_to_cart_button.click()

        # Step 5: Click the cart icon/button to open the shopping bag
        cart_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.cart-button'))
        )
        self.assertTrue(cart_button.is_displayed(), "Cart button is not visible.")
        cart_button.click()

        # Step 6: Verify that the "GO TO CHECKOUT" button is present inside the cart
        go_to_checkout_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/checkout"]'))
        )
        self.assertTrue(go_to_checkout_button.is_displayed(), "GO TO CHECKOUT button is not visible.")

        # Step 7: Click the "GO TO CHECKOUT" button
        go_to_checkout_button.click()

        # Step 8: Fill required checkout fields
        email_input = wait.until(
            EC.presence_of_element_located((By.ID, "customer.email"))
        )
        email_input.send_keys("mail@mail.com")

        phone_input = driver.find_element(By.ID, "customer.mobile")
        phone_input.send_keys("12345678")

        state_input = driver.find_element(By.ID, "shipping_address.state")
        state_input.send_keys("Riga")

        city_input = driver.find_element(By.ID, "shipping_address.city")
        city_input.send_keys("Riga")

        # Step 9: Select a shipping and payment method
        shipping_method = driver.find_element(By.CSS_SELECTOR, 'input[name="shipping_method_id"]')
        shipping_method.click()
        
        payment_method = driver.find_element(By.CSS_SELECTOR, 'input[name="payment_method_id"]')
        payment_method.click()

        # Step 10: Click "Next" and then "Place Order" to complete the process
        next_button = driver.find_element(By.CSS_SELECTOR, '.checkout-button-wrap .button')
        next_button.click()

        place_order_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.checkout-button-wrap button[type="submit"]'))
        )
        place_order_button.click()

        # Step 11: Confirm that the success page contains the message: "Thanks for your order!"
        success_message = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.checkout-success-title'))
        )
        self.assertIn("Thanks for your order!", success_message.text, "Success message not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()