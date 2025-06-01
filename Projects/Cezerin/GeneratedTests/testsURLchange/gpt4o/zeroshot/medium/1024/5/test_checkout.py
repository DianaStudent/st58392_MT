from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # 2. Click on "Category A"
        category_a = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a']")))
        category_a.click()

        # 3. Select the first product (Product A)
        product_a = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a/product-a']")))
        product_a.click()

        # 4. Click the "Add to cart" button
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Add to cart')]")))
        add_to_cart_button.click()

        # 5. Click the cart icon/button to open the shopping bag
        cart_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart-button")))
        cart_button.click()

        # 6. Verify that the "GO TO CHECKOUT" button is present inside the cart
        goto_checkout_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'GO TO CHECKOUT')]")))
        
        if not goto_checkout_button:
            self.fail("GO TO CHECKOUT button is not present in the cart.")

        # 7. Click the "GO TO CHECKOUT" button
        goto_checkout_button.click()

        # 8. Fill required checkout fields
        email_input = wait.until(EC.presence_of_element_located((By.ID, "customer.email")))
        mobile_input = wait.until(EC.presence_of_element_located((By.ID, "customer.mobile")))
        state_input = driver.find_element(By.ID, "shipping_address.state")
        city_input = driver.find_element(By.ID, "shipping_address.city")

        email_input.send_keys("mail@mail.com")
        mobile_input.send_keys("12345678")
        state_input.send_keys("Riga")
        city_input.send_keys("Riga")

        # 9. Select a shipping and payment method
        shipping_method = driver.find_element(By.XPATH, "//input[@name='shipping_method_id']")
        payment_method = driver.find_element(By.XPATH, "//input[@name='payment_method_id']")

        shipping_method.click()
        payment_method.click()

        # 10. Click "Next" and then "Place Order"
        next_button = driver.find_element(By.XPATH, "//button[text()='Next']")
        next_button.click()

        place_order_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Place Order']")))
        
        if not place_order_button:
            self.fail("Place Order button is not available after next step.")
        
        place_order_button.click()

        # 11. Confirm that the success page contains "Thanks for your order!"
        success_message = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Thanks for your order!')]")))
        
        if not success_message:
            self.fail("Order confirmation message not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()