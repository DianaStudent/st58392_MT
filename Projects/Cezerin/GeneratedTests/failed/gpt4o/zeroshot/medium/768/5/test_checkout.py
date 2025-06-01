from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.driver.implicitly_wait(10)

    def test_checkout_process(self):
        driver = self.driver

        # 1. Open home page
        driver.get("http://localhost:3000/") 

        # 2. Click on product category
        category_a_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/category-a"]'))
        )
        category_a_link.click()

        # 3. Select the first product
        product_a_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/category-a/product-a"]'))
        )
        product_a_link.click()

        # 4. Click the "Add to cart" button
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.button-addtocart button'))
        )
        add_to_cart_button.click()

        # 5. Click the cart icon/button to open the shopping bag.
        cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "cart-button"))
        )
        cart_button.click()

        # 6. Verify that the "GO TO CHECKOUT" button is present inside the cart.
        go_to_checkout_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Go to checkout"))
        )
        self.assertIsNotNone(go_to_checkout_button, "GO TO CHECKOUT button is not present.")

        # 7. Click the "GO TO CHECKOUT" button.
        go_to_checkout_button.click()

        # 8. Fill required checkout fields
        email_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "customer.email"))
        )
        email_field.send_keys("mail@mail.com")

        mobile_field = driver.find_element(By.ID, "customer.mobile")
        mobile_field.send_keys("12345678")

        state_field = driver.find_element(By.ID, "shipping_address.state")
        state_field.send_keys("Riga")

        city_field = driver.find_element(By.ID, "shipping_address.city")
        city_field.send_keys("Riga")

        # 9. Select a shipping and payment method.
        shipping_method = driver.find_element(By.CSS_SELECTOR, 'input[name="shipping_method_id"]')
        shipping_method.click()

        payment_method = driver.find_element(By.CSS_SELECTOR, 'input[name="payment_method_id"]')
        payment_method.click()

        # 10. Click "Next" and then "Place Order" to complete the process.
        next_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.checkout-button-wrap button[type="submit"]'))
        )
        next_button.click()        

        place_order_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Place Order"]'))
        )
        place_order_button.click()

        # 11. Confirm that the success page contains the message: "Thanks for your order!".
        success_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[text()="Thanks for your order!"]'))
        )
        self.assertIsNotNone(success_message, "Order success message is not present.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()