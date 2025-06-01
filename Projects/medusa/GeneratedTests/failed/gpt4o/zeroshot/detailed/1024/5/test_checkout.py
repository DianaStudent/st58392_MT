from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class TestCheckoutProcess(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Make sure ChromeDriver is in PATH
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Step 2: Click the menu button
        menu_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='nav-menu-button']")))
        menu_button.click()

        # Step 3: Click the "Store" link
        store_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-testid='store-link']")))
        store_link.click()

        # Step 4: Click on a product image (Thumbnail) - first product
        first_product_img = wait.until(EC.element_to_be_clickable((By.XPATH, "(//img[@alt='Thumbnail'])[1]")))
        first_product_img.click()

        # Step 5: Select size by clicking the size button "L"
        size_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='option-button' and text()='L']")))
        size_button.click()

        # Step 6: Add the product to the cart
        add_product_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='add-product-button' and text()='Add to cart']")))
        add_product_button.click()

        # Step 7: Explicitly click the cart button to open the cart
        cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-testid='nav-cart-link']")))
        cart_button.click()

        # Verify "GO TO CHECKOUT" button is present
        go_to_checkout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='go-to-cart-button']")))
        if not go_to_checkout_button:
            self.fail("GO TO CHECKOUT button is not present")

        go_to_checkout_button.click()

        # Step 8: Fill checkout fields
        first_name_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@data-testid='shipping-first-name-input']")))
        last_name_input = driver.find_element(By.XPATH, "//input[@data-testid='shipping-last-name-input']")
        address_input = driver.find_element(By.XPATH, "//input[@data-testid='shipping-address-input']")
        postal_code_input = driver.find_element(By.XPATH, "//input[@data-testid='shipping-postal-code-input']")
        city_input = driver.find_element(By.XPATH, "//input[@data-testid='shipping-city-input']")
        country_select = driver.find_element(By.XPATH, "//select[@data-testid='shipping-country-select']")
        email_input = driver.find_element(By.XPATH, "//input[@data-testid='shipping-email-input']")

        first_name_input.send_keys("user")
        last_name_input.send_keys("test")
        address_input.send_keys("street 1")
        postal_code_input.send_keys("LV-1021")
        city_input.send_keys("Riga")
        country_select.send_keys("Denmark")
        country_select.send_keys(Keys.ENTER)
        email_input.send_keys("user@test.com")

        # Step 9: Click "Continue to delivery"
        continue_to_delivery_button = driver.find_element(By.XPATH, "//button[@data-testid='submit-address-button']")
        continue_to_delivery_button.click()

        # Step 10: Select delivery method - radio button
        delivery_method = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@data-testid='radio-button'])[1]")))
        delivery_method.click()

        # Step 11: Click "Continue to payment"
        continue_to_payment_button = driver.find_element(By.XPATH, "//button[@data-testid='submit-delivery-option-button']")
        continue_to_payment_button.click()

        # Step 12: Select payment method - radio button
        payment_method = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@data-testid='radio-button'])[1]")))
        payment_method.click()

        # Step 13: Click "Continue to review"
        continue_to_review_button = driver.find_element(By.XPATH, "//button[@data-testid='submit-payment-button']")
        continue_to_review_button.click()

        # Step 14: Click "Place Order"
        place_order_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='submit-order-button']")))
        place_order_button.click()

        # Step 15: Verify the confirmation page
        order_confirmation_text = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@data-testid,'order-complete-container')]//span[text()='Your order was placed successfully.']")))
        self.assertIn("Your order was placed successfully", order_confirmation_text.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()