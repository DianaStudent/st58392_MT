import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open home page and click on the menu button
        menu_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='nav-menu-button']")))
        menu_button.click()

        # 2. Click on the "Store" link
        store_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@data-testid='store-link']")))
        store_link.click()

        # 3. Click on a product image (thumbnail)
        product_image = wait.until(EC.presence_of_element_located((By.XPATH, "//ul[@data-testid='products-list']/li/a/div/img")))
        product_image.click()

        # 4. Select a size
        size_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='option-button' and text()='L']")))
        size_button.click()

        # 5. Click the "Add to Cart" button
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='add-product-button' and text()='Add to cart']")))
        add_to_cart_button.click()

        # 6. Click the cart button to open the cart
        cart_button = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@data-testid='nav-cart-link']")))
        cart_button.click()

        # 7. Click "Go to checkout"
        go_to_checkout_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='go-to-cart-button']")))
        go_to_checkout_button.click()

        # 8. Fill checkout fields
        driver.find_element(By.XPATH, "//input[@data-testid='shipping-first-name-input']").send_keys("user")
        driver.find_element(By.XPATH, "//input[@data-testid='shipping-last-name-input']").send_keys("test")
        driver.find_element(By.XPATH, "//input[@data-testid='shipping-address-input']").send_keys("street 1")
        driver.find_element(By.XPATH, "//input[@data-testid='shipping-postal-code-input']").send_keys("LV-1021")
        driver.find_element(By.XPATH, "//input[@data-testid='shipping-city-input']").send_keys("Riga")
        driver.find_element(By.XPATH, "//select[@data-testid='shipping-country-select']").send_keys("Denmark")
        driver.find_element(By.XPATH, "//input[@data-testid='shipping-email-input']").send_keys("user@test.com")

        submit_address_button = driver.find_element(By.XPATH, "//button[@data-testid='submit-address-button']")
        submit_address_button.click()

        # 9. Select delivery method
        delivery_option = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@data-testid='delivery-option-radio'][1]/div/button")))
        delivery_option.click()
        submit_delivery_button = driver.find_element(By.XPATH, "//button[@data-testid='submit-payment-button']")
        submit_delivery_button.click()

        # 10. Select payment method and continue
        payment_option = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='headlessui-radio-:rk:']/div/div/button")))
        payment_option.click()
        submit_payment_button = driver.find_element(By.XPATH, "//button[@data-testid='submit-payment-button']")
        submit_payment_button.click()

        # 11. Click "Place Order"
        place_order_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='submit-order-button']")))
        place_order_button.click()

        # Verify confirmation page
        confirmation_message = wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@data-testid='order-complete-container']/h1/span[2]"))
        )
        self.assertIn("Your order was placed successfully", confirmation_message.text)

if __name__ == "__main__":
    unittest.main()