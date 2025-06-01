from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAddToCartProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # 1. Open home page
        # (Already done in setUp)

        # 2. Click the menu button ("Menu")
        menu_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']")))
        menu_button.click()

        # 3. Click the "Store" link
        store_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='store-link']")))
        store_link.click()

        # 4. Click on a product image (Thumbnail) - first product
        product_image = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img[alt='Thumbnail']")))
        product_image.click()

        # 5. Select size by clicking the size button "L"
        size_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='L']")))
        size_button.click()

        # 6. Add the product to the cart
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-product-button']")))
        add_to_cart_button.click()

        # 7. Explicitly click the cart button to open the cart
        cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-cart-link']")))
        cart_button.click()

        # 8. Click "Go to checkout"
        go_to_checkout_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='go-to-cart-button']")))
        go_to_checkout_button.click()

        # Fill checkout fields
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-testid='shipping-first-name-input']"))).send_keys("user")
        driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-last-name-input']").send_keys("test")
        driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-address-input']").send_keys("street 1")
        driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-postal-code-input']").send_keys("LV-1021")
        driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-city-input']").send_keys("Riga")
        
        country_select = driver.find_element(By.CSS_SELECTOR, "select[data-testid='shipping-country-select']")
        for option in country_select.find_elements_by_tag_name('option'):
            if option.text == 'Denmark':
                option.click()
                break

        driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-email-input']").send_keys("user@test.com")

        # 9. Click "Continue to delivery"
        continue_to_delivery_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit-address-button']")
        continue_to_delivery_button.click()

        # 10. Select delivery method - radio button
        delivery_option = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[data-testid='delivery-option-radio'] button")))
        delivery_option.click()

        # 11. Click "Continue to payment"
        continue_to_payment_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit-delivery-option-button']")
        continue_to_payment_button.click()

        # 12. Select payment method - radio button
        payment_option = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[id^='headlessui-radio-'] button")))
        payment_option.click()

        # 13. Click "Continue to review"
        continue_to_review_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit-payment-button']")
        continue_to_review_button.click()

        # 14. Click "Place Order"
        place_order_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-order-button']")))
        place_order_button.click()

        # 15. Verify the confirmation page contains: "Your order was placed successfully"
        confirmation_text_present = wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Your order was placed successfully"))
        self.assertTrue(confirmation_text_present, "Confirmation message not present")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()