from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.assertions import Assert

class TestECommerceWebsite(unittest.TestCase):
    def setUp(self):
        # Initialize the ChromeDriver using webdriver-manager
        from webdriver_manager.chrome import ChromeDriverManager
        driver = ChromeDriverManager().get_chrome_driver()
        
    def tearDown(self):
        # Close the ChromeDriver when done testing
        self.driver.quit()

    def test_add_to_cart(self):
        # Open the home page of the e-commerce website
        self.driver.get("http://localhost:8080/en/")
        
        # Click on a product category
        select_category = WebDriverWait(self.driver, 20).until(Select(self.driver.find_element_by_css_selector('ul>li>a')).get_attribute('href'))
        self.assertEqual(select_category, 'https://example.com/category')
        
        # Select the first product listed in the category
        product = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'First Product')]")))
        
        # Add the selected product to cart
        self.assertEqual(product.get_attribute('data-name'), 'Product 1')
        add_button = WebDriverWait(self.driver, 20).until(EC.element_located((By.XPATH, "//button[@id='add-to-cart']")))
        self.assertTrue(add_button.is_enabled(), "Add to Cart button is disabled")
        self.assertEqual(add_button.get_attribute("class"), 'btn btn-primary', "Button class does not match expected value")
        
        # Wait for the modal popup confirmation
        WebDriverWait(self.driver, 20).until(EC.element_located((By.XPATH, "//div[contains(text(), 'Product successfully added to your shopping cart')]")))
        
        # Verify the modal contains a message like "Product successfully added to your shopping cart"
        self.assertTrue(EC.text_to_be_present_in_element((By.XPATH, "//h2[contains(text(), 'Product successfully added to your shopping cart')]"))
)

if __name__ == '__main__':
    unittest.main()