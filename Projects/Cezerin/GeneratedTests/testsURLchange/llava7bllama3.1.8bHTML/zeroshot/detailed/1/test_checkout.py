from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestCheckout(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()

    def test_checkout(self):
        # Open home page
        self.driver.get("http://localhost:3000/")

        # Click on product category
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/products']"))).click()

        # Select the first product
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@class='product-title']/parent::div"))).click()

        # Click the "Add to cart" button
        self.driver.find_element(By.XPATH, "//button[@class='add-to-cart']").click()

        # Click the cart icon/button to open the shopping bag
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "(//a[@class='cart-button'])[1]"))).click()

        # Verify that the "GO TO CHECKOUT" button is present inside the cart
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[text()='GO TO CHECKOUT']"))))

        # Click the "GO TO CHECKOUT" button
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[text()='GO TO CHECKOUT']"))).click()

        # Wait for the checkout form to appear
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "checkout-form")))

        # Fill out the checkout form fields using the following credentials:
        self.driver.find_element(By.NAME, 'email').send_keys('mail@mail.com')
        self.driver.find_element(By.NAME, 'phone').send_keys('12345678')
        self.driver.find_element(By.NAME, 'state').send_keys('Riga')
        self.driver.find_element(By.NAME, 'city').send_keys('Riga')

        # Select a shipping method and a payment method
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "shipping-method"))).click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "payment-method"))).click()

        # Click the "Next" button
        self.driver.find_element(By.XPATH, "//button[@class='next-button']").click()

        # Click the "Place Order" button
        self.driver.find_element(By.XPATH, "//button[@class='place-order-button']").click()

        # Wait for the confirmation page and check that it includes the text "Thanks for your order!"
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h2[text()='Thank you for your order!']")))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()