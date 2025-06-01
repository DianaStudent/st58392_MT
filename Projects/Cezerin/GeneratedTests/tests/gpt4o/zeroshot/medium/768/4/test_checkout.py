import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestCheckoutProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000")
        self.driver.maximize_window()
    
    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 2: Click on product category
        category_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a']")))
        category_link.click()

        # Step 3: Select the first product
        product_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a/product-a']")))
        product_link.click()

        # Step 4: Click the "Add to cart" button
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add to cart')]")))
        add_to_cart_button.click()

        # Step 5: Click the cart icon/button to open the shopping bag
        cart_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart-button")))
        cart_button.click()

        # Step 6: Verify that the "GO TO CHECKOUT" button is present inside the cart
        go_to_checkout_button = wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'active') and contains(text(),'Go to checkout')]"))
        )
        self.assertIsNotNone(go_to_checkout_button)

        # Step 7: Click the "GO TO CHECKOUT" button
        go_to_checkout_button.click()

        # Step 8: Fill required checkout fields
        email_input = wait.until(EC.presence_of_element_located((By.ID, "customer.email")))
        email_input.send_keys("mail@mail.com")

        mobile_input = driver.find_element(By.ID, "customer.mobile")
        mobile_input.send_keys("12345678")

        state_input = driver.find_element(By.ID, "shipping_address.state")
        state_input.send_keys("Riga")

        city_input = driver.find_element(By.ID, "shipping_address.city")
        city_input.send_keys("Riga")

        # Step 9: Select a shipping and payment method
        shipping_method = driver.find_element(By.XPATH, "//input[@name='shipping_method_id']")
        if not shipping_method.is_selected():
            shipping_method.click()

        payment_method = driver.find_element(By.XPATH, "//input[@name='payment_method_id']")
        if not payment_method.is_selected():
            payment_method.click()

        # Step 10: Click "Next" and then "Place Order" to complete the process
        next_button = driver.find_element(By.XPATH, "//button[contains(text(),'Next')]")
        next_button.click()

        place_order_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Place Order')]")))
        place_order_button.click()

        # Step 11: Confirm that the success page contains the message: "Thanks for your order!"
        success_message = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Thanks for your order!')]")))
        self.assertIsNotNone(success_message)

if __name__ == "__main__":
    unittest.main()