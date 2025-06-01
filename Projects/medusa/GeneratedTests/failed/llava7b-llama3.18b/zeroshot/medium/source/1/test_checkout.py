from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestCheckout(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def test_checkout(self):
        # Click on the menu button
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='menu-btn']"))).click()

        # Click on the "Store" link
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='nav-menu']/li[2]/a"))).click()

        # Click on a product image (thumbnail)
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='product-grid-item']//img")))[0].click()

        # Select a size
        self.driver.find_element(By.ID, "size-select").send_keys("S")

        # Click the "Add to Cart" button
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='add-to-cart-btn']"))).click()

        # Wait for presence of "GO TO CHECKOUT" button using html_data.
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='cart-item']/a")))

        # Click the cart button to open the cart
        self.driver.find_element(By.ID, "cart-btn").click()

        # Click "Go to checkout"
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='go-to-checkout-btn']"))).click()

        # Fill required checkout fields
        self.driver.find_element(By.ID, "first-name").send_keys("user")
        self.driver.find_element(By.ID, "last-name").send_keys("test")
        self.driver.find_element(By.ID, "address").send_keys("street 1")
        self.driver.find_element(By.ID, "postal-code").send_keys("LV-1021")
        self.driver.find_element(By.ID, "city").send_keys("Riga")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//select[@id='country']"))).send_keys("Denmark")
        self.driver.find_element(By.ID, "email").send_keys("user@test.com")

        # Select delivery and payment methods
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='shipping-methods']/input")))[0].click()

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='place-order-btn']"))).click()

        # Verify the confirmation page contains: "Your order was placed successfully"
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='order-success-message']/h2")))
        self.assertEqual("Your order was placed successfully", self.driver.find_element(By.XPATH, "//div[@class='order-success-message']/h2").text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()