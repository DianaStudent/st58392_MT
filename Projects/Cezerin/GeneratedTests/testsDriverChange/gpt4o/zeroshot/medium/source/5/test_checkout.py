import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Open Category A
        category_a = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a']")))
        category_a.click()

        # Select the first product
        first_product = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a/product-a']")))
        first_product.click()

        # Click "Add to cart" button
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add to cart')]")))
        add_to_cart_button.click()

        # Click the cart icon/button to open the shopping bag
        cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-button img")))
        cart_button.click()

        # Verify "GO TO CHECKOUT" button is present
        go_to_checkout_button = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'GO TO CHECKOUT')]")))
        assert go_to_checkout_button is not None

        # Click "GO TO CHECKOUT" button
        go_to_checkout_button.click()

        # Fill required checkout fields
        email_field = wait.until(EC.presence_of_element_located((By.ID, "customer.email")))
        email_field.send_keys("mail@mail.com")
        
        mobile_field = driver.find_element(By.ID, "customer.mobile")
        mobile_field.send_keys("12345678")

        state_field = driver.find_element(By.ID, "shipping_address.state")
        state_field.send_keys("Riga")

        city_field = driver.find_element(By.ID, "shipping_address.city")
        city_field.send_keys("Riga")

        # Select shipping method
        shipping_method = driver.find_element(By.XPATH, "//input[@value='67ca982ef38a654a7c2c1a69']")
        shipping_method.click()

        # Select payment method
        payment_method = driver.find_element(By.XPATH, "//input[@value='67ca982ef38a654a7c2c1a6a']")
        payment_method.click()

        # Click "Next" button
        next_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Next')]")
        next_button.click()

        # Click "Place Order" button
        place_order_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Place Order')]")
        place_order_button.click()

        # Confirm the success page contains the text: "Thanks for your order!"
        success_message = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Thanks for your order!')]")))
        self.assertIsNotNone(success_message)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()