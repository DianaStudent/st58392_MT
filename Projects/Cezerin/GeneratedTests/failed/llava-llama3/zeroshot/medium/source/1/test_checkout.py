from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

class TestOrderPlacement(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().get_chrome_driver())
        
    def tearDown(self):
        self.driver.quit()
    
    def test_order_placement(self):
        self.driver.get("http://localhost:3000/")
        product_category = WebDriverWait(self.driver, 20).until(
            self.wait_for_visible_element((By.XPATH, "//a[contains(text(), 'Category A')]"))
        )
        first_product = WebDriverWait(self.driver, 20).until(
            self.wait_for_visible_element((By.XPATH, "//li/a[contains(@href, 'category-1')]"))
        )
        self.driver.execute_script(f"arguments[0].click(arguments[0]);", first_product)
        cart_button = WebDriverWait(self.driver, 20).until(
            self.wait_for_visible_element((By.XPATH, "//a[contains(text(), 'cart')]"))
        )
        self.driver.execute_script(f"arguments[0].click(arguments[0]);", cart_button)
        checkout_button = WebDriverWait(self.driver, 20).until(
            self.wait_for_visible_element((By.XPATH, "//li/a[contains(@href, 'checkout-1')]"))
        )
        self.driver.execute_script(f"arguments[0].click(arguments[0]);", checkout_button)
        email_field = WebDriverWait(self.driver, 20).until(
            self.wait_for_visible_element((By.XPATH, "//input[@name='email']"))
        )
        phone_field = WebDriverWait(self.driver, 20).until(
            self.wait_for_visible_element((By.XPATH, "//input[@name='phone']"))
        )
        shipping_address_field = WebDriverWait(self.driver, 20).until(
            self.wait_for_visible_element((By.XPATH, "//input[@name='shipping_address']"))
        )
        payment_method_field = WebDriverWait(self.driver, 20).until(
            self.wait_for_visible_element((By.XPATH, "//select[contains(@name, 'payment_method')]"))
        )
        self.driver.execute_script(f"arguments[0].click(arguments[0]);", checkout_button)
        order_placed = WebDriverWait(self.driver, 20).until(
            self.wait_for_page_load_complete()
        )
        success_message = WebDriverWait(self.driver, 20).until(
            self.wait_for_text("Thanks for your order!")
        )
        self.assertTrue(success_message, "Order confirmation message not found")
    
if __name__ == '__main__':
    unittest.main()