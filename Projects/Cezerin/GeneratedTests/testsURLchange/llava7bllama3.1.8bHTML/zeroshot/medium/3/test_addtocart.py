import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        # Open home page
        self.driver.get("http://localhost:3000/")  # replace with actual URL

        # Click on product category
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Category A"))
        ).click()

        # Select the first product
        product_name = self.driver.find_element_by_xpath("//h1[contains(text(), 'Product A')]")
        product_name.click()  # assuming it opens on click

        # Click the "Add to cart" button
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='button is-success is-fullwidth']"))
        ).click()

        # Click the cart icon/button to open the shopping bag
        self.driver.find_element_by_xpath("//a[@href='#' and @class='cart-button']").click()

        # Wait for presence of "GO TO CHECKOUT" button
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'GO TO CHECKOUT')]"))
        )

    def test_cart_icon_opened_mini_cart(self):
        self.driver.get("http://localhost:3000/")  # replace with actual URL

        # Click on product category
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Category A"))
        ).click()

        # Select the first product
        product_name = self.driver.find_element_by_xpath("//h1[contains(text(), 'Product A')]")
        product_name.click()  # assuming it opens on click

        # Click the "Add to cart" button
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='button is-success is-fullwidth']"))
        ).click()

        # Verify that the mini-cart opened by clicking the cart icon/button
        self.assertTrue(self.driver.find_element_by_xpath("//div[@class='mini-cart open']").is_displayed())

if __name__ == "__main__":
    unittest.main()