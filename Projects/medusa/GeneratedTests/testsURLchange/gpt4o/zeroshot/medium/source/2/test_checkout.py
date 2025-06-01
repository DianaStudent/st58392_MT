import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get('http://localhost:8000/dk')
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart_and_checkout(self):
        driver = self.driver

        # Open home page
        wait = self.wait

        # 1. Click on the menu button.
        menu_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="nav-menu-button"]')))
        menu_button.click()

        # 2. Click on the "Store" link.
        store_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="store-link"]')))
        store_link.click()

        # 3. Click on a product image (thumbnail).
        product_thumbnail = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ul[data-testid="products-list"] li a')))
        product_thumbnail.click()

        # 4. Select a size.
        size_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="option-button"]')))
        size_button.click()

        # 5. Click the "Add to Cart" button.
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="add-product-button"]')))
        add_to_cart_button.click()

        # 6. Click the cart button to open the cart.
        cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="nav-cart-link"]')))
        cart_button.click()

        # 7. Click "Go to checkout"
        go_to_checkout_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="go-to-cart-button"]')))
        go_to_checkout_button.click()

        # 8. Fill checkout fields:
        first_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="shipping-first-name-input"]')))
        first_name_input.send_keys("user")

        last_name_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="shipping-last-name-input"]')
        last_name_input.send_keys("test")

        address_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="shipping-address-input"]')
        address_input.send_keys("street 1")

        postal_code_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="shipping-postal-code-input"]')
        postal_code_input.send_keys("LV-1021")

        city_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="shipping-city-input"]')
        city_input.send_keys("Riga")

        country_select = driver.find_element(By.CSS_SELECTOR, 'select[data-testid="shipping-country-select"]')
        country_select.send_keys("Denmark")

        email_input = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="shipping-email-input"]')
        email_input.send_keys("user@test.com")

        continue_to_delivery_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="submit-address-button"]')
        continue_to_delivery_button.click()

        # 9. Select delivery and payment methods.
        delivery_button = wait.until(EC.presence_of_element_located((By.ID, 'headlessui-radio-:rh:')))
        delivery_button.click()

        continue_to_payment_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="submit-delivery-option-button"]')
        continue_to_payment_button.click()

        payment_button = wait.until(EC.presence_of_element_located((By.ID, 'headlessui-radio-:rk:')))
        payment_button.click()

        continue_to_review_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="submit-payment-button"]')
        continue_to_review_button.click()

        # 10. Click "Place Order".
        place_order_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="submit-order-button"]')))
        place_order_button.click()

        # 11. Verify the confirmation page contains: "Your order was placed successfully"
        confirmation_element = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Your order was placed successfully."]')))

        # Assert the confirmation text is present
        self.assertTrue(confirmation_element.is_displayed(), "Order confirmation message not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()