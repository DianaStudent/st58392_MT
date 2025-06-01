import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class CheckoutTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open home page (already done in setUp)
        
        # Step 2: Click on product category
        category_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a']")))
        category_link.click()

        # Step 3: Select the first product
        product_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a/product-a']")))
        product_link.click()

        # Step 4: Click the "Add to cart" button
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Add to cart')]")))
        add_to_cart_button.click()

        # Step 5: Click the cart icon/button to open the shopping bag
        cart_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart-button")))
        cart_button.click()

        # Step 6: Verify that the "GO TO CHECKOUT" button is present inside the cart
        go_to_checkout_button = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Go to checkout')]")))
        self.assertIsNotNone(go_to_checkout_button)

        # Step 7: Click the "GO TO CHECKOUT" button
        go_to_checkout_button.click()

        # Step 8: Wait for the checkout form to appear
        email_input = wait.until(EC.presence_of_element_located((By.ID, "customer.email")))

        # Step 9: Fill out the checkout form fields
        email_input.send_keys("mail@mail.com")
        mobile_input = driver.find_element(By.ID, "customer.mobile")
        mobile_input.send_keys("12345678")
        state_input = driver.find_element(By.ID, "shipping_address.state")
        state_input.send_keys("Riga")
        city_input = driver.find_element(By.ID, "shipping_address.city")
        city_input.send_keys("Riga")

        # Step 10: Select a shipping method and a payment method
        shipping_method = driver.find_element(By.XPATH, "//input[@name='shipping_method_id']")
        driver.execute_script("arguments[0].click();", shipping_method)
        payment_method = driver.find_element(By.XPATH, "//input[@name='payment_method_id']")
        driver.execute_script("arguments[0].click();", payment_method)

        # Step 11: Click the "Next" button
        next_button = driver.find_element(By.XPATH, "//button[contains(text(),'Next')]")
        next_button.click()

        # Step 12: Click the "Place Order" button
        place_order_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Place Order')]")))
        place_order_button.click()

        # Step 13: Wait for the confirmation page and check that it includes the text "Thanks for your order!"
        confirmation_message = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Thanks for your order!')]")))
        self.assertIsNotNone(confirmation_message)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()