import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

class TestAddToCart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://localhost:8080/en/')

    def test_add_to_cart(self):
        # Open a product category
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//li[@data-name="Shop"]'))).click()

        # Select the first product listed in the category
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//ul[@class="product-list"]/li[1]/a'))).click()

        # On the product detail page, click the "Add to cart" button
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@data-action="add-to-cart"]'))).click()

        # Wait for the modal popup that confirms the product was added to the cart
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'blockcart-modal')))

        # Verify the modal contains a message like "Product successfully added to your shopping cart"
        modal_title = self.driver.find_element(By.ID, 'myModalLabel').text
        self.assertIn('successfully', modal_title, msg='Modal title does not contain "successfully"')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()