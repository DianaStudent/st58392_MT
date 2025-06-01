import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open home page
        driver.get("http://localhost:3000/")

        # Step 2: Click on product category
        category_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/category-a']")))
        category_link.click()

        # Step 3: Select the first product
        first_product_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/category-a/product-a']")))
        first_product_link.click()

        # Step 4: Click the "Add to cart" button
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button.is-success.is-fullwidth")))
        add_to_cart_button.click()

        # Step 5: Click the cart icon/button to open the shopping bag
        cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-button")))
        cart_button.click()

        # Step 6: Verify that the "GO TO CHECKOUT" button is present inside the cart
        go_to_checkout_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/checkout']")))
        self.assertTrue(go_to_checkout_button.is_displayed(), "GO TO CHECKOUT button not found in cart.")

        # Step 7: Click the "GO TO CHECKOUT" button
        go_to_checkout_button.click()

        # Step 8: Fill required checkout fields
        email_field = wait.until(EC.presence_of_element_located((By.ID, "customer.email")))
        email_field.send_keys("mail@mail.com")

        mobile_field = driver.find_element(By.ID, "customer.mobile")
        mobile_field.send_keys("12345678")

        country_field = driver.find_element(By.ID, "shipping_address.country")
        state_field = driver.find_element(By.ID, "shipping_address.state")
        city_field = driver.find_element(By.ID, "shipping_address.city")

        country_field.clear()
        country_field.send_keys("SG")
        state_field.send_keys("Riga")
        city_field.send_keys("Riga")

        # Step 9: Select a shipping and payment method
        shipping_method = driver.find_element(By.CSS_SELECTOR, "input[type='radio'][name='shipping_method_id']")
        payment_method = driver.find_element(By.CSS_SELECTOR, "input[type='radio'][name='payment_method_id']")

        shipping_method.click()
        payment_method.click()

        # Step 10: Click "Next" and then "Place Order"
        next_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        next_button.click()

        place_order_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit'].is-primary")))
        place_order_button.click()

        # Step 11: Confirm that the success page contains the message: "Thanks for your order!"
        success_message = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Thanks for your order!')]")))
        self.assertTrue("Thanks for your order!" in success_message.text, "Order success message not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()