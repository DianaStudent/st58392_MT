from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestCheckoutProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_checkout_process(self):
        driver = self.driver

        # Open home page
        driver.get("http://localhost:3000/")
        wait = WebDriverWait(driver, 20)

        # Click on product category
        category_a = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Category A")))
        category_a.click()

        # Select the first product
        product_a = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a/product-a']")))
        product_a.click()

        # Click the "Add to cart" button
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to cart']")))
        add_to_cart_button.click()

        # Click the cart icon/button to open the shopping bag
        cart_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "cart-button")))
        cart_button.click()

        # Verify that the "GO TO CHECKOUT" button is present inside the cart
        try:
            go_to_checkout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "GO TO CHECKOUT")))
            self.assertTrue(go_to_checkout_button.is_displayed())
        except:
            self.fail("GO TO CHECKOUT button not found")

        # Click the "GO TO CHECKOUT" button
        go_to_checkout_button.click()

        # Fill required checkout fields
        email_field = wait.until(EC.element_to_be_clickable((By.NAME, "email")))
        email_field.send_keys("test@example.com")

        mobile_field = wait.until(EC.element_to_be_clickable((By.NAME, "mobile")))
        mobile_field.send_keys("123456789")

        state_field = driver.find_element(By.NAME, "shipping_address.state")
        state_field.send_keys("Riga")

        city_field = driver.find_element(By.NAME, "shipping_address.city")
        city_field.send_keys("Riga")

        # Select a shipping and payment method
        shipping_method = driver.find_element(By.XPATH, "//input[@name='shipping_method_id']")
        shipping_method.click()

        payment_method = driver.find_element(By.XPATH, "//input[@name='payment_method_id']")
        payment_method.click()

        # Click "Next"
        next_button = driver.find_element(By.XPATH, "//button[text()='Next']")
        next_button.click()

        # Click "Place Order"
        place_order_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Place Order']")))
        place_order_button.click()

        # Confirm that the success page contains the message: "Thanks for your order!"
        try:
            success_message = wait.until(EC.presence_of_element_located(
                (By.XPATH, "//h1[contains(text(), 'Thanks for your order!')]")))
            self.assertTrue(success_message.is_displayed())
        except:
            self.fail("Success message not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()