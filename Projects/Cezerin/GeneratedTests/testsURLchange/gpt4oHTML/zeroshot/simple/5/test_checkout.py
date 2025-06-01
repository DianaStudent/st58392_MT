from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class CheckoutProcessTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("http://localhost:3000/")
    
    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        try:
            # Navigate to the product page
            product_a = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a/product-a']")))
            product_a.click()
            
            # Add product to cart
            add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add to cart')]")))
            add_to_cart_button.click()
            
            # Click cart button (shopping bag)
            cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='cart-button']/img[@title='cart']")))
            cart_button.click()
            
            # Wait for presence of "GO TO CHECKOUT" button
            go_to_checkout = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@class='button is-primary is-fullwidth has-text-centered active' and @href='/checkout']")))
            go_to_checkout.click()
            
            # Fill required checkout fields
            email_field = wait.until(EC.presence_of_element_located((By.ID, "customer.email")))
            email_field.send_keys("mail@mail.com")
            
            mobile_field = driver.find_element(By.ID, "customer.mobile")
            mobile_field.send_keys("12345678")
            
            country_field = driver.find_element(By.ID, "shipping_address.country")
            country_field.send_keys("SG")
            
            state_field = driver.find_element(By.ID, "shipping_address.state")
            state_field.send_keys("Riga")
            
            city_field = driver.find_element(By.ID, "shipping_address.city")
            city_field.send_keys("Riga")
            
            shipping_method = driver.find_element(By.XPATH, "//input[@name='shipping_method_id' and @value='67ca982ef38a654a7c2c1a69']")
            shipping_method.click()
            
            payment_method = driver.find_element(By.XPATH, "//input[@name='payment_method_id' and @value='67ca982ef38a654a7c2c1a6a']")
            payment_method.click()
            
            # Clicking Next to proceed
            next_button = driver.find_element(By.XPATH, "//button[@class='checkout-button button is-primary' and @type='submit']")
            next_button.click()
            
            # Place the order
            place_order_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='checkout-button button is-primary' and @type='submit']")))
            place_order_button.click()
            
            # Confirm success page
            success_message = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[@class='checkout-success-title']/img/following-sibling::br/following-sibling::text()='Thanks for your order!']")))
            
            self.assertTrue(success_message.is_displayed(), "Success message not displayed")

        except Exception as e:
            self.fail("Test failed due to an exception: " + str(e))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()