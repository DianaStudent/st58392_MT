import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("about:blank")  # Simulating the opening of a home page.

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open home page.
        driver.get("http://example.com")  # Use actual home page URL here.

        # 2. Click on product category.
        category_a = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a']")))
        category_a.click()

        # 3. Select the first product.
        first_product = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a/product-a']")))
        first_product.click()

        # 4. Click the "Add to cart" button.
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'button-addtocart')]//*[text()='Add to cart']/parent::button")))
        add_to_cart_button.click()

        # 5. Click the cart icon/button to open the shopping bag.
        cart_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "cart-button")))
        cart_button.click()

        # 6. Verify that the "GO TO CHECKOUT" button is present inside the cart.
        go_to_checkout_button = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/checkout' and contains(text(), 'Go to checkout')]")))
        self.assertTrue(go_to_checkout_button.is_displayed(), msg="GO TO CHECKOUT button is not present.")

        # 7. Click the "GO TO CHECKOUT" button.
        go_to_checkout_button.click()

        # 8. Wait for the checkout form to appear.
        checkout_form = wait.until(EC.presence_of_element_located((By.XPATH, "//form")))

        # 9. Fill out the checkout form fields using the provided credentials.
        email_input = wait.until(EC.presence_of_element_located((By.ID, "customer.email")))
        mobile_input = driver.find_element(By.ID, "customer.mobile")
        state_input = driver.find_element(By.ID, "shipping_address.state")
        city_input = driver.find_element(By.ID, "shipping_address.city")

        email_input.send_keys("mail@mail.com")
        mobile_input.send_keys("12345678")
        state_input.send_keys("Riga")
        city_input.send_keys("Riga")

        # 10. Select a shipping method and a payment method.
        shipping_method_radio = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='shipping_method_id']")))
        payment_method_radio = driver.find_element(By.XPATH, "//input[@name='payment_method_id']")

        shipping_method_radio.click()
        payment_method_radio.click()

        # 11. Click the "Next" button.
        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Next']")))
        next_button.click()

        # 12. Click the "Place Order" button.
        place_order_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Place Order']")))
        place_order_button.click()

        # 13. Wait for the confirmation page and check for the confirmation text.
        confirmation_text = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Thanks for your order!')]")))
        
        self.assertTrue(confirmation_text.is_displayed(), msg="'Thanks for your order!' message not displayed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()