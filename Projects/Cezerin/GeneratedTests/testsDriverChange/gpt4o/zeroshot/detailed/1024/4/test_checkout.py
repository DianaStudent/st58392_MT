import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class CheckoutTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.driver.maximize_window()

    def test_checkout_process(self):
        driver = self.driver

        # Open home page and click on Category A
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a']"))
        ).click()

        # Click on the first product in Category A
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a/product-a']"))
        ).click()

        # Click the "Add to cart" button
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".button-addtocart button"))
        ).click()

        # Open the mini-cart by clicking the cart icon (shopping bag)
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-button"))
        ).click()

        # Verify that the "GO TO CHECKOUT" button is present
        checkout_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "GO TO CHECKOUT"))
        )
        self.assertTrue(checkout_button.is_displayed())

        # Click the "GO TO CHECKOUT" button
        checkout_button.click()

        # Fill out the checkout form
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "customer.email"))
        ).send_keys("mail@mail.com")

        driver.find_element(By.ID, "customer.mobile").send_keys("12345678")
        driver.find_element(By.ID, "shipping_address.state").send_keys("Riga")
        driver.find_element(By.ID, "shipping_address.city").send_keys("Riga")

        # Select a shipping method
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='shipping_method_id']"))
        ).click()

        # Select a payment method
        driver.find_element(By.CSS_SELECTOR, "input[name='payment_method_id']").click()

        # Click the "Next" button
        driver.find_element(By.CSS_SELECTOR, ".checkout-button-wrap .button").click()

        # Click the "Place Order" button
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']"))
        ).click()

        # Confirm success page contains "Thanks for your order!"
        success_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout-success-details .checkout-success-title"))
        )
        self.assertIn("Thanks for your order!", success_message.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()