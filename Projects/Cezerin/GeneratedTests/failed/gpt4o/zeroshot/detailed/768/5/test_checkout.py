from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestCheckoutProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.driver.maximize_window()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Step 1: Open home page
        driver.get("http://localhost:3000/")

        # Step 2: Click on product category
        category_a_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/category-a']")))
        category_a_link.click()

        # Step 3: Select the first product
        product_a_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/category-a/product-a']")))
        product_a_link.click()

        # Step 4: Click the "Add to cart" button
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-addtocart button")))
        add_to_cart_button.click()

        # Step 5: Click the cart icon/button to open the shopping bag
        cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-button")))
        cart_button.click()

        # Step 6: Verify that the "GO TO CHECKOUT" button is present inside the cart
        go_to_checkout_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/checkout']")))
        self.assertTrue(go_to_checkout_button.is_displayed(), "GO TO CHECKOUT button is not present")

        # Step 7: Click the "GO TO CHECKOUT" button
        go_to_checkout_button.click()

        # Step 8: Wait for the checkout form to appear
        email_field = wait.until(EC.element_to_be_clickable((By.ID, "customer.email")))

        # Step 9: Fill out the checkout form fields using the following credentials
        email_field.send_keys("mail@mail.com")

        phone_field = driver.find_element(By.ID, "customer.mobile")
        phone_field.send_keys("12345678")

        state_field = driver.find_element(By.ID, "shipping_address.state")
        state_field.send_keys("Riga")

        city_field = driver.find_element(By.ID, "shipping_address.city")
        city_field.send_keys("Riga")

        # Step 10: Select a shipping method and a payment method
        shipping_method = driver.find_element(By.CSS_SELECTOR, "input[name='shipping_method_id']")
        shipping_method.click()

        payment_method = driver.find_element(By.CSS_SELECTOR, "input[name='payment_method_id']")
        payment_method.click()

        # Step 11: Click the "Next" button
        next_button = driver.find_element(By.CSS_SELECTOR, ".checkout-button-wrap .button")
        next_button.click()

        # Step 12: Click the "Place Order" button
        place_order_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button.is-primary")))
        place_order_button.click()

        # Step 13: Wait for the confirmation page and check that it includes the text "Thanks for your order!"
        confirmation_message = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Thanks for your order!')]")))
        self.assertTrue(confirmation_message.is_displayed(), "Confirmation text not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()