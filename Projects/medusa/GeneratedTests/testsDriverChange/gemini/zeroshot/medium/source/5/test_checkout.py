import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebElement

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8000/dk")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver

        # 1. Open home page.
        self.assertEqual(driver.current_url, "http://localhost:8000/dk")

        # 2. Click on the menu button.
        menu_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']"))
        )
        menu_button.click()

        # 3. Click on the "Store" link.
        store_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='store-link']"))
        )
        store_link.click()

        # 4. Click on a product image (thumbnail).
        product_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/dk/products/sweatshirt']"))
        )
        product_link.click()

        # 5. Select a size.
        size_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='option-button'][text()='L']"))
        )
        size_button.click()

        # 6. Click the "Add to Cart" button.
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-product-button']"))
        )
        add_to_cart_button.click()

        # 7. Click the cart button to open the cart.
        cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id='headlessui-popover-button-:Rrmdtt7:']"))
        )
        cart_button.click()

        # 8. Click "Go to checkout", fill checkout fields:
        go_to_checkout_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='go-to-cart-button']"))
        )
        go_to_checkout_button.click()

        go_to_checkout_button2 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='checkout-button'] > button"))
        )
        go_to_checkout_button2.click()

        first_name_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='shipping-first-name-input']"))
        )
        first_name_input.send_keys("user")

        last_name_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='shipping-last-name-input']"))
        )
        last_name_input.send_keys("test")

        address_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='shipping-address-input']"))
        )
        address_input.send_keys("street 1")

        postal_code_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='shipping-postal-code-input']"))
        )
        postal_code_input.send_keys("LV-1021")

        city_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='shipping-city-input']"))
        )
        city_input.send_keys("Riga")

        country_select = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "select[data-testid='shipping-country-select']"))
        )
        country_select.click()
        country_option = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "option[value='dk']"))
        )
        country_option.click()

        email_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='shipping-email-input']"))
        )
        email_input.send_keys("user@test.com")

        submit_address_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-address-button']"))
        )
        submit_address_button.click()

        # 9. Select delivery and payment methods.
        delivery_option = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@data-testid='delivery-option-radio'][.//span[text()='Express Shipping']]//button[@data-testid='radio-button']"))
        )
        delivery_option.click()

        submit_delivery_option_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-delivery-option-button']"))
        )
        submit_delivery_option_button.click()

        payment_option = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@id='headlessui-radio-:rk:']//button[@data-testid='radio-button']"))
        )
        payment_option.click()

        submit_payment_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-payment-button']"))
        )
        submit_payment_button.click()

        # 10. Click "Place Order".
        submit_order_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-order-button']"))
        )
        submit_order_button.click()

        # 11. Verify the confirmation page contains: "Your order was placed successfully"
        confirmation_text_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@data-testid='order-complete-container']/h1/span[1]"))
        )
        confirmation_text = confirmation_text_element.text if isinstance(confirmation_text_element, WebElement) else None

        if confirmation_text:
            self.assertEqual(confirmation_text, "Thank you!")
        else:
            self.fail("Confirmation text not found or is empty.")

if __name__ == "__main__":
    unittest.main()