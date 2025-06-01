from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestProductAddToCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_add_product_to_cart(self):
        # Open the home page.
        self.driver.get("http://localhost:8080/en/")

        # Click on a product category from the top navigation menu (e.g. ART).
        art_category_link = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "ART"))
        )
        art_category_link.click()

        # Wait for the category page to load.
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".col-sm-4"))
        )

        # Click on the first product in the list.
        first_product_link = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "The best is yet to come' Framed poster"))
        )
        first_product_link.click()

        # On the product detail page, click the "Add to cart" button.
        add_to_cart_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-primary"))
        )
        add_to_cart_button.click()

        # Wait for the modal popup to appear after the product is added.
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "blockcart-modal"))
        )

        # Confirm that the modal title or content includes a success message like "successfully added".
        modal_title = self.driver.find_element(By.CSS_SELECTOR, ".modal-title").text
        if not ("added" in modal_title.lower() and "successfully" in modal_title.lower()):
            self.fail("Modal title does not include 'successfully added' text.")

        # Optionally, locate and assert the presence of a "Proceed to checkout" button inside the modal.
        proceed_to_checkout_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-primary"))
        )
        if not self.driver.execute_script("return arguments[0].getAttribute('href') != null", proceed_to_checkout_button):
            self.fail("Proceed to checkout button is missing.")

if __name__ == '__main__':
    unittest.main()