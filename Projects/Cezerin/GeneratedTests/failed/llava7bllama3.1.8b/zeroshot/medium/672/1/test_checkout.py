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

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        # Open home page
        self.driver.get("http://localhost:3000/")

        # Click on product category (Assuming "Category A" is the first category)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a']"))).click()

        # Select the first product
        self.driver.find_element(By.XPATH, "//div[@class='product-list']//a[1]").click()

        # Click "Add to cart" button
        self.driver.find_element(By.XPATH, "//button[text()='Add to Cart']").click()

        # Open shopping bag (Cart) and verify presence of "GO TO CHECKOUT" button
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-button"))).click()
        cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='mini-cart']//a[text()='GO TO CHECKOUT']")))
        self.assertTrue(cart_button.is_displayed())

        # Click "GO TO CHECKOUT" button
        cart_button.click()

        # Fill required checkout fields
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "checkout-email"))).send_keys("test@example.com")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "checkout-phone"))).send_keys("1234567890")

        # Fill Shipping details
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "shipping_address[address1]"))).send_keys("123 Main St")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "shipping_address[city]"))).send_keys("Anytown")

        # Select a shipping method
        self.driver.find_element(By.XPATH, "//input[@value='Ground']").click()

        # Select a payment method
        self.driver.find_element(By.XPATH, "//input[@value='Credit Card']").click()

        # Place order
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "commit"))).click()

        # Verify success page contains message: "Thanks for your order!"
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='success-message']")))
        self.assertEqual(self.driver.find_element(By.XPATH, "//div[@class='success-message']").text, "Thanks for your order!")

if __name__ == '__main__':
    unittest.main()