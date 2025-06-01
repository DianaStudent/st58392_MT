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
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait
        
        # 1. Open home page
        driver.get("http://localhost:3000/")
        
        # 2. Click on product category
        category_link = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[@href='/category-a']")))
        category_link.click()

        # 3. Select the first product
        product_link = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[@href='/category-a/product-a']")))
        product_link.click()

        # 4. Click the "Add to cart" button
        add_to_cart_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[text()='Add to cart']")))
        add_to_cart_button.click()

        # 5. Click the cart icon/button to open the shopping bag
        cart_button = wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, "cart-button")))
        cart_button.click()

        # 6. Verify that the "GO TO CHECKOUT" button is present inside the cart
        go_to_checkout_button = wait.until(EC.element_to_be_clickable(
            (By.LINK_TEXT, "GO TO CHECKOUT")))

        if not go_to_checkout_button:
            self.fail("Go to checkout button is not present.")

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
        shipping_method = driver.find_element(By.XPATH, "//input[@value='67ca982ef38a654a7c2c1a69']")
        shipping_method.click()
        
        payment_method = driver.find_element(By.XPATH, "//input[@value='67ca982ef38a654a7c2c1a6a']")
        payment_method.click()

        # 10. Click "Next" and then "Place Order" to complete the process
        next_button = driver.find_element(By.XPATH, "//button[text()='Next']")
        next_button.click()

        place_order_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[text()='Place Order']")))
        place_order_button.click()

        # 11. Confirm that the success page contains the message: "Thanks for your order!"
        success_message = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//h1[contains(text(),'Thanks for your order!')]")))

        if not success_message:
            self.fail("Order success message not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()