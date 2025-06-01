import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAddToCart(unittest.TestCase):
    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        # Open the home page.
        self.driver.get("http://localhost:8080/en/")

        # Click on a product category (e.g. from the top menu).
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Products"))
        ).click()

        # Select the first product listed in the category.
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='product-name']"))
        ).click()

        # On the product detail page, click the "Add to cart" button.
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='add-to-cart']"))
        ).click()

        # Wait for the modal popup that confirms the product was added to the cart.
        self.modal_title = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "modal-title"))
        )
        self.assertEqual("Product successfully added to your shopping cart", self.modal_title.text.strip())

if __name__ == "__main__":
    unittest.main()