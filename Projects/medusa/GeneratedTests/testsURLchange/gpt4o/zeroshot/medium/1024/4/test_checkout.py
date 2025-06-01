import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class MedusaStoreTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8000/dk")

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open home page
        self.assertIn("Ecommerce Starter Template", driver.page_source)

        # Step 2: Click on the menu button
        menu_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']")))
        menu_button.click()

        # Step 3: Click on the "Store" link
        store_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='store-link']")))
        store_link.click()

        # Step 4: Click on a product image (thumbnail)
        product_image = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul[data-testid='products-list'] li a img")))
        product_image.click()

        # Step 5: Select a size
        size_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='option-button']")))
        size_button.click()

        # Step 6: Click the "Add to cart" button
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='add-product-button']")))
        add_to_cart_button.click()

        # Step 7: Click the cart button to open the cart
        cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-cart-link']")))
        cart_button.click()

        # Step 8: Click "Go to checkout"
        go_to_checkout_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='go-to-cart-button']")))
        go_to_checkout_button.click()

        # Step 8: Fill checkout fields
        self.fill_checkout_fields(driver, wait)

        # Step 9: Select delivery and payment methods & continue to review
        delivery_option = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='delivery-option-radio'] button")))
        delivery_option.click()

        continue_to_payment_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit-delivery-option-button']")
        continue_to_payment_button.click()

        payment_option = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[id^='headlessui-radio'] button")))
        payment_option.click()

        continue_to_review_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit-payment-button']")
        continue_to_review_button.click()

        # Step 10: Click "Place Order"
        place_order_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='submit-order-button']")))
        place_order_button.click()

        # Step 11: Verify the confirmation page
        success_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='order-complete-container'] h1 span:nth-child(2)")))
        self.assertIn("Your order was placed successfully", success_message.text)

    def fill_checkout_fields(self, driver, wait):
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='shipping-first-name-input']"))).send_keys("user")
        driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-last-name-input']").send_keys("test")
        driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-address-input']").send_keys("street 1")
        driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-postal-code-input']").send_keys("LV-1021")
        driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-city-input']").send_keys("Riga")
        driver.find_element(By.CSS_SELECTOR, "select[data-testid='shipping-country-select'] option[value='dk']").click()
        driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-email-input']").send_keys("user@test.com")
        driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit-address-button']").click()

if __name__ == "__main__":
    unittest.main()