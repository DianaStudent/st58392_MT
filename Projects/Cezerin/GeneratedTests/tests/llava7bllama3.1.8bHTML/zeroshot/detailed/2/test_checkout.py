import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_shopping_cart(self):
        # Step 1: Open home page
        self.driver.get('http://localhost:8000')  # replace with your URL or remove this line if it's an absolute path

        # Step 2: Click on product category
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Category A'))).click()

        # Step 3: Select the first product
        product_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/product/product-a']"))).get_attribute('href')
        self.driver.get(product_link)

        # Step 4: Click the "Add to cart" button.
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'add-to-cart'))).click()

        # Step 5: Click the cart icon/button to open the shopping bag
        cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-button")))
        cart_button.click()

        # Step 6: Verify that the "GO TO CHECKOUT" button is present inside the cart.
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-primary' and contains(text(), 'GO TO CHECKOUT')]")))

        # Step 7: Click the "GO TO CHECKOUT" button
        go_to_checkout_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary' and contains(text(), 'GO TO CHECKOUT')]")))
        go_to_checkout_button.click()

        # Step 8: Wait for the checkout form to appear
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'email')))

        # Step 9: Fill out the checkout form fields using the following credentials:
        email_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'email')))
        phone_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'phone')))

        state_select = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'state-select')))
        city_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'city')))

        email_input.send_keys('mail@mail.com')
        phone_input.send_keys('12345678')

        # Step 10: Select a shipping method and a payment method
        state_select.click()
        self.driver.find_element(By.XPATH, "//option[@value='Riga']").click()

        city_input.send_keys('Riga')

        # Wait for payment methods to load (you may need to adjust this)
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'payment-select')))

        self.driver.find_element(By.XPATH, "//option[@value='card']").click()

        # Step 11: Click the "Next" button
        next_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary' and contains(text(), 'Next')]")))
        next_button.click()

        # Step 12: Click the "Place Order" button
        place_order_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary' and contains(text(), 'Place Order')]")))
        place_order_button.click()

        # Step 13: Wait for the confirmation page and check that it includes the text "Thanks for your order!"
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Thanks for your order!')]")))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()