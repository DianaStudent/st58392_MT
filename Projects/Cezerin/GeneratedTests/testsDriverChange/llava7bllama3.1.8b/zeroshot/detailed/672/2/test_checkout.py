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
        # Click on product category and select the first product
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/category']"))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='product-list-item']"))).click()

        # Click the "Add to cart" button
        self.driver.find_element(By.ID, 'add-to-cart').click()

        # Click the cart icon/button to open the shopping bag
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='cart-button']"))).click()
        
        # Verify that the "GO TO CHECKOUT" button is present inside the cart
        self.driver.find_element(By.XPATH, "//button[text()='GO TO CHECKOUT']").is_enabled()

        # Click the "GO TO CHECKOUT" button
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='GO TO CHECKOUT']"))).click()
        
        # Fill out the checkout form fields using the following credentials:
        self.driver.find_element(By.ID, 'email').send_keys('mail@mail.com')
        self.driver.find_element(By.ID, 'phone').send_keys('12345678')
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='state']"))).click()
        self.driver.find_element(By.XPATH, "//select[@name='shipping_state']").send_keys('Riga')
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='city']"))).click()
        self.driver.find_element(By.XPATH, "//select[@name='shipping_city']").send_keys('Riga')

        # Select a shipping method and a payment method
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[text()='Next Day Delivery']"))).click()

        # Click the "Next" button
        self.driver.find_element(By.ID, 'next').click()
        
        # Click the "Place Order" button
        self.driver.find_element(By.ID, 'place-order').click()
        
        # Wait for the confirmation page and check that it includes the text "Thanks for your order!"
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element((By.XPATH, "//h1"), 'Thanks for your order!'))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()