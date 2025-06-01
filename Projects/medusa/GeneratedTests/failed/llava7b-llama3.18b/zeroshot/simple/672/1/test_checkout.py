from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class CheckoutSimpleTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_checkout_simple(self):
        driver = self.driver
        driver.get("http://localhost:8000/dk")

        # Adding a product to the cart
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='ADD TO CART']"))
        ).click()

        # Clicking on the cart button
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='SHOPPING BAG']"))
        )
        driver.find_element(By.XPATH, "//a[contains(text(), 'CHECKOUT')]")

        # Filling required checkout fields
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='email']"))
        ).send_keys("test@example.com")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='phone']"))
        ).send_keys("1234567890")

        # Filling shipping address
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='address_line_1']"))
        ).send_keys("123 Main St")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='city']"))
        ).send_keys("Anytown")

        # Filling payment information
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='card_number']"))
        ).send_keys("1234567890123456")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='expiration_date']"))
        ).send_keys("12/2025")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='CVV']"))
        ).send_keys("123")

        # Placing the order
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='PLACE ORDER']"))
        ).click()

        # Verifying that the final success page contains the required text
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Your order was placed successfully')]"))
        )

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()