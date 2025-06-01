import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def tearDown(self):
        self.driver.quit()

    def test_shopping_cart_process(self):
        # Open home page.
        self.driver.get("http://localhost/")

        # Click on product category.
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/category']"))
        ).click()

        # Select the first product.
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//h3/a[1]"))
        ).click()

        # Click the "Add to cart" button.
        self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()

        # Click the cart icon/button to open the shopping bag. 
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-button"))
        ).click()

        # Verify that the "GO TO CHECKOUT" button is present inside the cart.
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-primary'][contains(text(), 'GO TO CHECKOUT')]"))
        )

        # Click the "GO TO CHECKOUT" button.
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary'][contains(text(), 'GO TO CHECKOUT')]").click()

        # Fill required checkout fields
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "email"))
        ).send_keys("test@example.com")
        
        self.driver.find_element(By.ID, "phone").send_keys("1234567890")

        self.driver.find_element(By.XPATH, "//input[@name='shippingAddress']").send_keys("104 N Stagecoach Rd Dover Foxcroft ME 04426")

        # Select a shipping and payment method.
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "shippingMethod"))
        ).click()

        self.driver.find_element(By.ID, "paymentMethod").click()

        # Click "Next" and then "Place Order" to complete the process.
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary'][contains(text(), 'Next')]"))
        ).click()
        
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary'][contains(text(), 'Place Order')]").click()

        # Confirm that the final success page contains the message: "Thanks for your order!".
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Thank you')]"))
        )
        
        self.assertEqual("Thanks for your order!", self.driver.find_element(By.XPATH, "//h2").text)

if __name__ == "__main__":
    unittest.main()