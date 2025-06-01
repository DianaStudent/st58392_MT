from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager

class TestCheckoutFlow(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('http://localhost:3000/')

    def test_checkout_flow(self):
        # Click on product category
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/category']"))).click()

        # Select the first product
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='products']/li[1]/div/a"))).click()

        # Click the "Add to cart" button
        self.driver.find_element(By.XPATH, "//button[@data-action='add-to-cart']").click()

        # Click the cart icon/button to open the shopping bag.
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-button"))).click()

        # Verify that the "GO TO CHECKOUT" button is present inside the cart.
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@href='#' and contains(text(), 'GO')]")))

        # Click the "GO TO CHECKOUT" button.
        self.driver.find_element(By.XPATH, "//a[@href='#' and contains(text(), 'GO')]").click()

        # Wait for the checkout form to appear.
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'checkout-form')))

        # Fill out the checkout form fields using the following credentials:
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("mail@mail.com")
        self.driver.find_element(By.XPATH, "//input[@name='phone']").send_keys("12345678")
        self.driver.find_element(By.XPATH, "//select[@name='state']").find_element_by_xpath("//option[text()='Riga']").click()
        self.driver.find_element(By.XPATH, "//input[@name='city']").send_keys("Riga")

        # Select a shipping method and a payment method.
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[@class='shipping-method']/div"))).click()

        self.driver.find_element(By.XPATH, "//a[@href='#' and contains(text(), 'Next')]").click()

        # Click the "Place Order" button.
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

        # Wait for the confirmation page
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h2[text()='Thanks for your order!']")))
        
        self.assertTrue("Thanks for your order!" in self.driver.page_source)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()