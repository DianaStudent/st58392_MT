import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def test_add_to_cart(self):
        # Click on the menu button
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.xpath("//button[@class='header-actions__menu-trigger']")))).click()

        # Click on the "Store" link
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Store']").click()

        # Click on a product image (thumbnail)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='Product Image']"))).click()

        # Select a size
        self.driver.find_element(By.XPATH, "//select[@name='size']/option[2]").click()  # Replace with actual option value

        # Click the "Add to Cart" button
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='product-action__add-to-cart']"))).click()

        # Click on the cart button (shopping bag)
        self.driver.find_element(By.XPATH, "//a[@class='header-actions__cart']").click()

        # Wait for presence of "GO TO CHECKOUT" button
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='GO TO CHECKOUT']")))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()