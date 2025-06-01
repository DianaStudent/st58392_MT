import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000")
        self.driver.maximize_window()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Open home page and click on product category
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/category-a']"))).click()
        
        # Select the first product
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/category-a/product-a']"))).click()
        
        # Click the "Add to cart" button
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-addtocart button"))).click()
        
        # Open the shopping bag
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-button img[title='cart']"))).click()
        
        # Verify that the "GO TO CHECKOUT" button is present inside the cart
        go_to_checkout_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/checkout']")))
        self.assertTrue(go_to_checkout_btn is not None)
        
        # Click the "GO TO CHECKOUT" button
        go_to_checkout_btn.click()
        
        # Wait for the checkout form to appear
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='email']")))

        # Fill out the checkout form fields
        driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("mail@mail.com")
        driver.find_element(By.CSS_SELECTOR, "input[name='mobile']").send_keys("12345678")
        driver.find_element(By.CSS_SELECTOR, "input[name='shipping_address.state']").send_keys("Riga")
        driver.find_element(By.CSS_SELECTOR, "input[name='shipping_address.city']").send_keys("Riga")

        # Select a shipping method and a payment method
        driver.find_element(By.CSS_SELECTOR, "input[name='shipping_method_id']").click()
        driver.find_element(By.CSS_SELECTOR, "input[name='payment_method_id']").click()

        # Click the "Next" button
        driver.find_element(By.CSS_SELECTOR, ".checkout-button-wrap button[type='submit']").click()

        # Click the "Place Order" button
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout-step h1 span:nth-child(2)")))
        driver.find_element(By.CSS_SELECTOR, ".checkout-button-wrap button[type='submit']").click()

        # Wait for the confirmation page and check that it includes the text "Thanks for your order!"
        thank_you_text = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout-success-title")))
        self.assertIn("Thanks for your order!", thank_you_text.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()