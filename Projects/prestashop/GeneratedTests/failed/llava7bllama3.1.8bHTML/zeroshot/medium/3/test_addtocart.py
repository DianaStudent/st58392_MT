from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class TestAddProductToCart(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('start-maximized')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost:8080/en/")

    def test_add_product_to_cart(self):
        # Click on a product category
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@data-name='Product Category']"))).click()

        # Select the first product listed in the category
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "(//ul[@class='product-grid-list']/li)[1]/a"))).click()

        # Click the "Add to cart" button on the product detail page
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-name='Add to cart']"))).click()

        # Wait for and verify the modal popup that confirms the product was added to the cart
        modal_title = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "(//h4)[1]")))
        self.assertEqual(modal_title.text, 'Product successfully added to your shopping cart')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()