import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCheckoutFlow(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        from webdriver_manager.chrome import ChromeDriverManager
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_checkout_flow(self):
        # Navigate to the application and add a product to cart
        self.driver.get("http://localhost:3000/")  # replace with your actual url
        self.driver.find_element(By.XPATH, "//button[@class='add-to-cart']").click()

        # Click on the cart button (shopping bag)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//i[@class='shopping-bag']"))).click()

        # Wait for presence of "GO TO CHECKOUT" button
        self.driver.find_element(By.XPATH, "//button[@id='go-to-checkout-button']").click()

        # Fill required checkout fields (e.g. email, phone, shipping address, Shipping, payment)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "email"))).send_keys("test@example.com")
        self.driver.find_element(By.NAME, "phone").send_keys("(207) 564-8482")
        self.driver.find_element(By.ID, "shipping-address").send_keys("104 N Stagecoach Rd, Dover Foxcroft, ME, 04426")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='shipping-method']"))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, "payment"))).send_keys("PayPal")

        # Place the order
        self.driver.find_element(By.ID, "place-order-button").click()

        # Confirm that the final success page contains the text: "Thanks for your order!"
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element((By.XPATH, "//h1"), "Thanks for your order!"))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()