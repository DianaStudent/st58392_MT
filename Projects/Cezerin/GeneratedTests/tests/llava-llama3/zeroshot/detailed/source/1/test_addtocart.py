import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

class TestAddToCart(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Chrome(ChromeDriverManager().get_chrome_driver())
        self.driver = driver

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        # Open home page
        self.driver.get('http://localhost:3000/')

        # Click on product category. (e.g. Category A)
        category_name = self.get_text_from_button("Category")
        self.category_click(category_name)

        # Select the first product. (e.g. Product A)
        product_name = self.get_text_from_button("Product A")
        self.product_click(product_name)

        # Click the "Add to cart" button
        self.add_to_cart()

        # Wait for mini-cart to become visible
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Shopping cart')]"))
        )

        # Verify that the "GO TO CHECKOUT" button is present inside the cart
        self.assertTrue(EC.text_to_be_visible("GO TO CHECKOUT"), "GO TO CHECKOUT not visible")

def get_text_from_button(self, text):
    """Get the text from a button in the specified element"""
    return EC.text_to_be_clickable((By.XPATH, "//button[contains(text(), '{}'')".format(text)))

def add_to_cart(self):
    """Add the product to cart"""
    # Find the "ADD TO CART" button
    add_to_cart_button = self.find_add_to_cart_button()

    if add_to_cart_button:
        # Click on the "ADD TO CART" button
        add_to_cart_button.click()
    
def category_click(self, category_name):
    """Click on a product category"""
    # Find the category button
    category_button = self.find_category_button(category_name)

    if category_button:
        # Click on the category button
        category_button.click()

def product_click(self, product_name):
    """Click on a product"""
    # Find the product button
    product_button = self.find_product_button(product_name)

    if product_button:
        # Click on the product button
        product_button.click()

def find_add_to_cart_button(self):
    """Find the 'ADD TO CART' button"""
    add_to_cart_button = WebDriverWait(self.driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'ADD TO CART')]"))
    )
    return add_to_cart_button

def find_category_button(self, category_name):
    """Find the category button based on a given category name"""
    category_button = WebDriverWait(self.driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Category') and contains(text(), '{}'))]".format(category_name)))
    return category_button

def find_product_button(self, product_name):
    """Find the product button based on a given product name"""
    product_button = WebDriverWait(self.driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Product') and contains(text(), '{}'))]".format(product_name)))
    return product_button

if __name__ == '__main__':
    unittest.main()