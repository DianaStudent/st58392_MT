from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:3000/")  # Replace with the actual home URL

    def test_checkout_process(self):
        driver = self.driver

        # 1. Open home page
        wait = WebDriverWait(driver, 20)
        
        # 2. Click on product category
        category_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a']")))
        category_link.click()

        # 3. Select the first product
        first_product = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a/product-a']")))
        first_product.click()

        # 4. Click the "Add to cart" button
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add to cart')]")))
        add_to_cart_button.click()

        # 5. Click the cart icon/button to open the shopping bag
        cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-button")))
        cart_button.click()

        # 6. Verify that the "GO TO CHECKOUT" button is present inside the cart
        go_to_checkout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Go to checkout')]")))
        
        if not go_to_checkout_button:
            self.fail("GO TO CHECKOUT button is not present in the cart")
        
        # 7. Click the "GO TO CHECKOUT" button
        go_to_checkout_button.click()

        # 8. Fill required checkout fields
        email_input = wait.until(EC.element_to_be_clickable((By.ID, "customer.email")))
        email_input.send_keys("mail@mail.com")
        
        mobile_input = driver.find_element(By.ID, "customer.mobile")
        mobile_input.send_keys("12345678")

        state_input = driver.find_element(By.ID, "shipping_address.state")
        state_input.send_keys("Riga")

        city_input = driver.find_element(By.ID, "shipping_address.city")
        city_input.send_keys("Riga")

        # 9. Select a shipping and payment method
        shipping_method = driver.find_element(By.XPATH, "//input[@name='shipping_method_id'][@value='67ca982ef38a654a7c2c1a69']")
        driver.execute_script("arguments[0].scrollIntoView(true);", shipping_method)
        shipping_method.click()

        payment_method = driver.find_element(By.XPATH, "//input[@name='payment_method_id'][@value='67ca982ef38a654a7c2c1a6a']")
        payment_method.click()

        # 10. Click "Next" and then "Place Order" to complete the process
        next_button = driver.find_element(By.XPATH, "//button[@class='checkout-button button is-primary'][contains(text(),'Next')]")
        next_button.click()

        place_order_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='checkout-button button is-primary'][contains(text(),'Place Order')]")))
        place_order_button.click()

        # 11. Confirm that the success page contains the message: "Thanks for your order!"
        success_message = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Thanks for your order!')]")))
        
        if not success_message:
            self.fail("Success message 'Thanks for your order!' not found on the final page")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()