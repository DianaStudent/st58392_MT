import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


class CheckoutProcessTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open home page
        driver.get("data:text/html;charset=utf-8,{home_page_html}".format(home_page_html=html_data["home_page"]))

        # Step 2: Click on product category
        category_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-a']")))
        category_link.click()

        # Step 3: Select the first product
        product_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-a/product-a']")))
        product_link.click()

        # Step 4: Click the "Add to cart" button
        add_to_cart_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Add to cart')]")))
        add_to_cart_button.click()

        # Step 5: Click the cart icon/button to open the shopping bag
        cart_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart-button")))
        cart_button.click()

        # Step 6: Verify that the "GO TO CHECKOUT" button is present inside the cart
        go_to_checkout_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Go to checkout']")))

        # Step 7: Click the "GO TO CHECKOUT" button
        go_to_checkout_button.click()

        # Step 8: Wait for the checkout form to appear
        email_input = wait.until(EC.visibility_of_element_located((By.ID, "customer.email")))

        # Step 9: Fill out the checkout form fields
        email_input.send_keys("mail@mail.com")
        phone_input = driver.find_element(By.ID, "customer.mobile")
        phone_input.send_keys("12345678")
        state_input = driver.find_element(By.ID, "shipping_address.state")
        state_input.send_keys("Riga")
        city_input = driver.find_element(By.ID, "shipping_address.city")
        city_input.send_keys("Riga")

        # Step 10: Select a shipping method and a payment method
        shipping_method_radio = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='shipping_method_id']")))
        shipping_method_radio.click()

        payment_method_radio = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='payment_method_id']")))
        payment_method_radio.click()

        # Step 11: Click the "Next" button
        next_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit' and contains(text(), 'Next')]")))
        next_button.click()

        # Step 12: Click the "Place Order" button
        place_order_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit' and contains(text(), 'Place Order')]")))
        place_order_button.click()

        # Step 13: Wait for the confirmation page and check that it includes the text "Thanks for your order!"
        success_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Thanks for your order!')]")))
        self.assertIn("Thanks for your order!", success_message.text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()