from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8000/dk")

    def test_checkout_process(self):
        driver = self.driver

        # Open home page and click the menu button ("Menu").
        menu_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']"))
        )
        menu_button.click()

        # Click the "Store" link.
        store_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='store-link']"))
        )
        store_link.click()

        # Click on a product image (Thumbnail) - first product.
        first_product = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "ul[data-testid='products-list'] li a"))
        )
        first_product.click()

        # Select size by clicking the size button "L".
        size_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='L']"))
        )
        size_button.click()

        # Add the product to the cart.
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-product-button']"))
        )
        add_to_cart_button.click()

        # Explicitly click the cart button.
        cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-cart-link']"))
        )
        cart_button.click()

        # Wait for "Go to checkout" button and click it.
        go_to_checkout_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='go-to-cart-button']"))
        )
        go_to_checkout_button.click()

        # Fill checkout fields.
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-first-name-input']"))
        ).send_keys('user')
        driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-last-name-input']").send_keys('test')
        driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-address-input']").send_keys('street 1')
        driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-postal-code-input']").send_keys('LV-1021')
        driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-city-input']").send_keys('Riga')
        select_country = driver.find_element(By.CSS_SELECTOR, "select[data-testid='shipping-country-select']")
        for option in select_country.find_elements(By.TAG_NAME, 'option'):
            if option.text == 'Denmark':
                option.click()
                break
        driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-email-input']").send_keys('user@test.com')

        # Click "Continue to delivery"
        driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit-address-button']").click()

        # Select delivery method - radio button and continue
        delivery_option = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "span[data-testid='delivery-option-radio']"))
        )
        delivery_option.click()
        driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit-delivery-option-button']").click()

        # Select payment method - radio button and continue
        payment_option = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "span[data-testid='delivery-option-radio']"))
        )
        payment_option.click()
        driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit-payment-button']").click()

        # Place order
        place_order_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-order-button']"))
        )
        place_order_button.click()

        # Verify the confirmation page.
        confirmation_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Your order was placed successfully')]"))
        )

        if not confirmation_message:
            self.fail('Confirmation message not found.')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()