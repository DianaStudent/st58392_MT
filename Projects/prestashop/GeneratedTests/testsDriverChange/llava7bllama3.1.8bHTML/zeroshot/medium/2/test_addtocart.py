import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_add_to_cart(self):
        # Click on a product category
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@data-name='Categories']"))
        ).click()

        # Select the first product listed in the category
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "(//div[@class='col-md-3 col-xs-4 col-sm-6'])[1]"))
        ).click()

        # On the product detail page, click the "Add to cart" button
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-name='Add to Cart']"))
        ).click()

        # Wait for the modal popup that confirms the product was added to the cart
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "blockcart-modal"))
        )

        # Verify the modal contains a message like "Product successfully added to your shopping cart"
        modal_title = self.driver.find_element(By.XPATH, "//h4[@class='modal-title']").text
        self.assertIn("successfully added", modal_title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()