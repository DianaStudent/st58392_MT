from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestCheckoutProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Open home page and click on the menu button
        menu_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']")))
        menu_button.click()

        # Click on the "Store" link
        store_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='store-link']")))
        store_link.click()

        # Click on a product image (thumbnail)
        product_image = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "img[alt='Thumbnail']")))
        product_image.click()

        # Select a size
        size_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='option-button']")))
        size_button.click()

        # Click the "Add to Cart" button
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='add-product-button']")))
        add_to_cart_button.click()

        # Click the cart button to open the cart
        cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-cart-link']")))
        cart_button.click()

        # Click "Go to checkout"
        go_to_checkout_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='go-to-cart-button']")))
        go_to_checkout_button.click()

        # Fill in checkout fields
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='shipping-first-name-input']"))).send_keys("user")
        driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-last-name-input']").send_keys("test")
        driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-address-input']").send_keys("street 1")
        driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-postal-code-input']").send_keys("LV-1021")
        driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-city-input']").send_keys("Riga")
        country_select = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[data-testid='shipping-country-select']")))
        country_select.send_keys("Denmark")
        driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-email-input']").send_keys("user@test.com")

        # Select delivery and payment methods
        delivery_option = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='delivery-option-radio'] > div > button")))
        delivery_option.click()
        continue_to_payment_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit-delivery-option-button']")
        continue_to_payment_button.click()

        payment_option = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[id^='headlessui-radiogroup'] button[data-testid='radio-button']")))
        payment_option.click()
        continue_to_review_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit-payment-button']")
        continue_to_review_button.click()

        # Click "Place Order"
        place_order_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='submit-order-button']")))
        place_order_button.click()

        # Verify the confirmation page contains: "Your order was placed successfully"
        success_message = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Your order was placed successfully.']")))
        self.assertIsNotNone(success_message, "Order success message is missing or empty")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()