import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://example.com") # Replace with the actual URL of the site
        self.driver.maximize_window()

    def test_checkout_process(self):
        driver = self.driver

        # Step 1: Navigate to Category A
        category_a_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a']"))
        )
        category_a_link.click()
        
        # Step 2: Click on Product A
        product_a_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a/product-a']"))
        )
        product_a_link.click()

        # Step 3: Add to cart
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Add to cart')]"))
        )
        add_to_cart_button.click()

        # Step 4: Click on cart button
        cart_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span.cart-button img[alt='Close']"))
        )
        cart_button.click()

        # Step 5: Wait for "GO TO CHECKOUT" button and click
        go_to_checkout_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Go to checkout')]"))
        )
        go_to_checkout_button.click()

        # Step 6: Fill the checkout form
        email_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "customer.email"))
        )
        email_input.send_keys("mail@mail.com")
        
        mobile_input = driver.find_element(By.ID, "customer.mobile")
        mobile_input.send_keys("12345678")
        
        state_input = driver.find_element(By.ID, "shipping_address.state")
        state_input.send_keys("Riga")
        
        city_input = driver.find_element(By.ID, "shipping_address.city")
        city_input.send_keys("Riga")

        shipping_method = driver.find_element(By.XPATH, "//input[@name='shipping_method_id' and @value='67ca982ef38a654a7c2c1a69']")
        shipping_method.click()

        payment_method = driver.find_element(By.XPATH, "//input[@name='payment_method_id' and @value='67ca982ef38a654a7c2c1a6a']")
        payment_method.click()

        # Step 7: Click on the "Next" button
        next_button = driver.find_element(By.CSS_SELECTOR, ".checkout-button-wrap .button.is-primary")
        next_button.click()

        # Step 8: Confirm order placement on final success page
        success_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Thanks for your order!')]"))
        )
        self.assertIn("Thanks for your order!", success_message.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()