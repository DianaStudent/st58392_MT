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
        self.driver.maximize_window()

    def test_checkout_process(self):
        driver = self.driver
        
        # Step 1: Open home page (already done in setUp)

        # Step 2: Click on product category
        category_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a']"))
        )
        category_link.click()

        # Step 3: Select the first product
        product_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a/product-a']"))
        )
        product_link.click()

        # Step 4: Click the "Add to cart" button
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Add to cart')]"))
        )
        add_to_cart_button.click()

        # Step 5: Click the cart icon/button to open the shopping bag
        cart_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='cart-button']"))
        )
        cart_button.click()

        # Step 6: Verify that the "GO TO CHECKOUT" button is present inside the cart
        go_to_checkout_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'GO TO CHECKOUT')]"))
        )
        self.assertIsNotNone(go_to_checkout_button, "GO TO CHECKOUT button not found")

        # Step 7: Click the "GO TO CHECKOUT" button
        go_to_checkout_button.click()

        # Step 8: Wait for the checkout form to appear
        email_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "customer.email"))
        )

        # Step 9: Fill out the checkout form fields
        email_field.send_keys("mail@mail.com")
        driver.find_element(By.ID, "customer.mobile").send_keys("12345678")
        driver.find_element(By.ID, "shipping_address.state").send_keys("Riga")
        driver.find_element(By.ID, "shipping_address.city").send_keys("Riga")

        # Step 10: Select a shipping method and a payment method
        shipping_method_radio = driver.find_element(By.XPATH, "//input[@name='shipping_method_id']")
        payment_method_radio = driver.find_element(By.XPATH, "//input[@name='payment_method_id']")
        shipping_method_radio.click()
        payment_method_radio.click()

        # Step 11: Click the "Next" button
        next_button = driver.find_element(By.XPATH, "//button[text()='Next']")
        next_button.click()

        # Step 12: Click the "Place Order" button
        place_order_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Place Order']"))
        )
        place_order_button.click()

        # Step 13: Wait for the confirmation page and check that it includes the text
        confirmation_text = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Thanks for your order!')]"))
        )
        self.assertIsNotNone(confirmation_text, "Order confirmation message not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()