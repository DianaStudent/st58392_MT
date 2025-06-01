from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium.webdriver.chrome.service import Service as ChromeService

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.driver.maximize_window()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to Category A
        category_a_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Category A")))
        category_a_link.click()

        # Select Product A
        product_a_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Product A")))
        product_a_link.click()

        # Add Product A to cart
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to cart']")))
        add_to_cart_button.click()

        # Open cart
        cart_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "cart-button")))
        cart_button.click()

        # Go to checkout
        checkout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "GO TO CHECKOUT")))
        checkout_button.click()

        # Fill in checkout details
        email_field = wait.until(EC.element_to_be_clickable((By.NAME, "email")))
        email_field.send_keys("mail@mail.com")

        mobile_field = driver.find_element(By.NAME, "mobile")
        mobile_field.send_keys("12345678")

        state_field = driver.find_element(By.NAME, "shipping_address.state")
        state_field.send_keys("Riga")

        city_field = driver.find_element(By.NAME, "shipping_address.city")
        city_field.send_keys("Riga")

        # Select Shipping and Payment methods
        shipping_method = driver.find_element(By.CSS_SELECTOR, "input[name='shipping_method_id'][value='67ca982ef38a654a7c2c1a69']")
        shipping_method.click()

        payment_method = driver.find_element(By.CSS_SELECTOR, "input[name='payment_method_id'][value='67ca982ef38a654a7c2c1a6a']")
        payment_method.click()

        # Submit Checkout Form
        next_button = driver.find_element(By.XPATH, "//button[text()='Next']")
        next_button.click()

        # Place order
        place_order_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Place Order']")))
        place_order_button.click()

        # Verify success page
        success_message = wait.until(
            EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Thanks for your order!')]"))
        )

        self.assertTrue(success_message is not None, "Order success message not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()