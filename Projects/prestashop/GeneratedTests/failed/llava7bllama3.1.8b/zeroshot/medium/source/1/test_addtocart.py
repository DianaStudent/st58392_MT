from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAddToCart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path='/path/to/chromedriver'
        )
        self.driver.get('http://localhost:8080/en/')

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        # Open the home page
        url = 'http://localhost:8080/en/'
        self.driver.get(url)

        # Click on a product category (e.g. from the top menu)
        categories_menu = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//ul[@class='nav-menu']"))
        )
        product_category = categories_menu.find_element(By.XPATH, "(//a)[1]")
        product_category.click()

        # Select the first product listed in the category
        products_list = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "products-list"))
        )
        first_product = products_list.find_elements(By.XPATH, ".//li")[0]
        add_to_cart_button = first_product.find_element(By.XPATH, ".//button")
        add_to_cart_button.click()

        # Wait for the modal popup that confirms the product was added to the cart
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "cart-modal"))
        )

        # Verify the modal contains a message like "Product successfully added to your shopping cart"
        cart_modal = self.driver.find_element(By.ID, "cart-modal")
        title = cart_modal.find_element(By.XPATH, ".//h2").text
        self.assertIn("successfully added", title)

if __name__ == '__main__':
    unittest.main()