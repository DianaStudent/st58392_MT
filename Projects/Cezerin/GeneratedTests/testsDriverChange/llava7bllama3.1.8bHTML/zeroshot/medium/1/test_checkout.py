import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class TestOrderFlow(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    def tearDown(self):
        self.driver.quit()

    def test_order_flow(self):
        self.driver.get("http://localhost:3000/")  # replace with your home page URL

        # Click on product category
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/category']"))).click()

        # Select the first product
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='product-name'])[1]"))).click()

        # Click the "Add to cart" button
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Add to Cart']"))).click()

        # Click the cart icon/button to open the shopping bag.
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-button"))).click()

        # Verify that the "GO TO CHECKOUT" button is present inside the cart
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@class='go-to-checkout']")))

        # Click the "GO TO CHECKOUT" button
        self.driver.find_element(By.XPATH, "//a[@class='go-to-checkout']").click()

        # Fill required checkout fields
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "email_address"))).send_keys("your_email")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "phone_number"))).send_keys("your_phone")

        # Select a shipping and payment method
        self.driver.find_element(By.XPATH, "//input[@name='shipping-address-line-1']").send_keys("your_shipping_address")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "s_method_free"))).click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@name='payment-method']"))).send_keys("your_payment_method")

        # Click "Next" and then "Place Order"
        self.driver.find_element(By.XPATH, "//button[@data-role='opc-continue']").click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@title='Place Order']"))).click()

        # Confirm that the final success page contains the text: "Thanks for your order!"
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Thank you')]")))
        self.assertTrue("Thanks for your order!" in self.driver.page_source)

if __name__ == "__main__":
    unittest.main()