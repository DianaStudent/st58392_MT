import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestCheckoutProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("file:///path/to/home_page.html")  # Replace with the actual path to the home_page HTML
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Assert home page is loaded
        home_page_element = driver.find_element(By.CSS_SELECTOR, "div#app")
        self.assertIsNotNone(home_page_element, "Home page did not load properly.")

        # Step 2: Click on product category
        category_link = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.has-items[href='/category-a']"))
        )
        category_link.click()

        # Step 3: Select the first product
        product_link = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/category-a/product-a']"))
        )
        product_link.click()

        # Step 4: Click the "Add to cart" button
        add_to_cart_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button.is-success.is-fullwidth"))
        )
        add_to_cart_button.click()

        # Step 5: Click the cart icon/button to open the shopping bag
        cart_button = driver.find_element(By.CSS_SELECTOR, "span.cart-button > img[title='cart']")
        cart_button.click()

        # Step 6: Verify that the "GO TO CHECKOUT" button is present inside the cart
        go_to_checkout_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a.button.is-primary.is-fullwidth"))
        )
        self.assertIsNotNone(go_to_checkout_button, "GO TO CHECKOUT button is not present in the cart.")

        # Step 7: Click the "GO TO CHECKOUT" button
        go_to_checkout_button.click()

        # Step 8: Wait for the checkout form to appear
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.checkout-form")))

        # Step 9: Fill out the checkout form fields
        driver.find_element(By.ID, "customer.email").send_keys("mail@mail.com")
        driver.find_element(By.ID, "customer.mobile").send_keys("12345678")
        driver.find_element(By.ID, "shipping_address.state").send_keys("Riga")
        driver.find_element(By.ID, "shipping_address.city").send_keys("Riga")

        # Step 10: Select a shipping method and a payment method
        shipping_method = driver.find_element(By.CSS_SELECTOR, "input[name='shipping_method_id']")
        payment_method = driver.find_element(By.CSS_SELECTOR, "input[name='payment_method_id']")
        shipping_method.click()
        payment_method.click()

        # Step 11: Click the "Next" button
        next_button = driver.find_element(By.CSS_SELECTOR, "button.checkout-button.is-primary")
        next_button.click()

        # Step 12: Click the "Place Order" button
        place_order_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.checkout-button.is-primary"))
        )
        place_order_button.click()

        # Step 13: Wait for the confirmation page and check that it includes the text "Thanks for your order!"
        confirmation_text = wait.until(
            EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Thanks for your order!')]"))
        )
        self.assertIsNotNone(confirmation_text, "'Thanks for your order!' text is not present on the confirmation page.")

if __name__ == "__main__":
    unittest.main()