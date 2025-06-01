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
        self.driver.get("http://localhost:3000/")

    def test_checkout_process(self):
        # Click on product category
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Category A']"))).click()

        # Select the first product
        product = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/product/1']")))
        product.click()

        # Click the "Add to cart" button
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to Cart']"))).click()

        # Open shopping bag
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-button"))).click()

        # Verify "GO TO CHECKOUT" button is present inside the cart
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='GO TO CHECKOUT']")))

        # Click the "GO TO CHECKOUT" button
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='GO TO CHECKOUT']"))).click()

        # Fill out checkout form fields using given credentials
        email_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='email']")))
        phone_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='phone']")))

        state_select = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='state']")))
        city_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='city']")))
        address_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//textarea[@name='address']")))

        email_input.send_keys("mail@mail.com")
        phone_input.send_keys("12345678")

        state_select.select_by_visible_text("Riga")
        city_input.send_keys("Riga")
        address_input.send_keys("Address")

        # Select a shipping method and a payment method
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='shipping-method-1']"))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='payment-method-1']"))).click()

        # Click the "Next" button
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Next']"))).click()

        # Click the "Place Order" button
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Place Order']"))).click()

        # Wait for confirmation page and check that it includes the text "Thanks for your order!"
        confirmation_text = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Thanks for your order!']")))
        self.assertEqual(confirmation_text.text.strip(), "Thanks for your order!")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()