from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

class TestAddProductToCart(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Chrome()
        self.driver = driver
        self.driver.get("http://localhost:8080/en/")

    def tearDown(self):
        self.driver.quit()

    def test_add_product_to_cart(self):
        # Step 1: Open the home page
        element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "header[1]")))
        element = self.driver.find_element_by_xpath("header[1]")
        element.click()

        # Step 2: Click on a product category from the top navigation menu
        categories = self.driver.find_elements_by_tag_name('ul')
        for cat in categories:
            if 'ART' in cat.text:
                cat.click()
                break

        # Step 3: Wait for the category page to load
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "header[2]")))

        # Step 4: Click on the first product in the list
        products = self.driver.find_elements_by_tag_name('figure')
        product = products[0]
        product.click()

        # Step 5: On the product detail page, click the "Add to cart" button
        add_to_cart_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Add to cart')]")))
        add_to_cart_button.click()

        # Step 6: Wait for the modal popup to appear after the product is added
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "div[@class='modal-dialog']")))

        # Step 7: Confirm that the modal title or content includes a success message like "successfully added"
        modal_title = self.driver.find_element_by_xpath("h4[@id='myModalLabel']")
        self.assertTrue('Successfully' in modal_title.text)

        # Optionally, locate and assert the presence of a "Proceed to checkout" button inside the modal
        proceed_to_checkout_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Proceed to checkout')]")))
        self.assertTrue(proceed_to_checkout_button is not None)

if __name__ == '__main__':
    unittest.main()