from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestCheckoutFlow(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost:3000/')

    def tearDown(self):
        self.driver.quit()

    def test_checkout_flow(self):
        # Click on product category
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/category']"))).click()
        
        # Select the first product and add it to cart
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//ul/li[1]/div/a"))).click()
        self.driver.find_element_by_xpath("//button[contains(text(), 'Add to cart')]").click()

        # Open shopping bag and verify "GO TO CHECKOUT" button
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-button"))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'GO TO CHECKOUT')]")))
        
        # Click "GO TO CHECKOUT" button
        self.driver.find_element_by_xpath("//button[contains(text(), 'GO TO CHECKOUT')]").click()

        # Fill out checkout form fields
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "email"))).send_keys("mail@mail.com")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "phone"))).send_keys("12345678")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[@name='state']"))).send_keys("Riga")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='text' and @placeholder='City']"))).send_keys("Riga")

        # Select shipping method and payment method
        self.driver.find_element_by_xpath("//select[@name='shipping_method']").click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//option[contains(text(), 'Free Shipping')]"))).click()

        self.driver.find_element_by_xpath("//input[@type='radio' and @value='paypal']").click()

        # Click "Next" button
        self.driver.find_element_by_xpath("//button[contains(text(), 'Next')]").click()

        # Place order
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Place Order')]"))).click()

        # Wait for confirmation page and check that it includes the text "Thanks for your order!"
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Thanks for your order!')]")))
        
        self.assertTrue(self.driver.find_element_by_xpath("//p[contains(text(), 'Thanks for your order!')]").is_displayed())

if __name__ == "__main__":
    unittest.main()