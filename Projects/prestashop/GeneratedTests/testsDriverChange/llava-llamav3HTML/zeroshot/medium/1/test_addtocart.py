```
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from html_data import HTMLData
class TestSeleniumTest(unittest.TestCase):
    def setUp(self):
        driver = ChromeDriverManager().get_chrome_driver()
        self.driver = driver

    def tearDown(self):
        self.driver.quit()

    def test_selenium_test(self):
        # Open the home page.
        self.driver.get(HTMLData.base_url + "home")

        # Click on a product category
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text('Home')]"))))
        )
        category = self.driver.find_elements_by_xpath("//*[contains(text('Home'])")
        for cat in category:
            if cat.text == "Category":
                break

        # Select the first product listed in the category
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text('The best is yet to come')")]")))
        first_product = self.driver.find_elements_by_xpath("//*[contains(text('The best is yet to come'))]")

        # Click on the product
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text('Framed'))]")))
        product = first_product[0]
        self.product = product

        # Add the product to cart
        add_to_cart_button = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text('Add to cart'))]")))
        add_to_cart_button.click()

        # Wait for the modal popup that confirms the product was added to the cart.
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='modal fade in']/div[@class='modal-dialog']") and By.XPATH,
                "//*[contains(text('Product successfully added to your shopping cart'))]"))
        modal = self.driver.find_elements_by_xpath("//div[@class='modal fade in']/div[@class='modal-dialog']")
        for m in modal:
            if m.text == "Product successfully added to your shopping cart":
                break

        # Verify the modal contains a message like  "Product successfully added to your shopping cart".
        self.assertTrue(
```