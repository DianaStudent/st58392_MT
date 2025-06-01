import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestAddToCartProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.base_url = "http://localhost:8080"

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Visit the home page
        driver.get(self.base_url + "/en/")

        # Click on the 'Art' category
        art_category_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Art")))
        art_category_link.click()

        # Click on the product 'The best is yet to come Framed poster'
        product_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "The best is yet to come'...")))
        product_link.click()

        # Wait for the product page to load and click 'Add to cart'
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn-primary.add-to-cart")))
        add_to_cart_button.click()

        # Wait for the success modal to appear
        modal_title = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'h4.modal-title'))
        )

        # Check for the success message in the modal
        if "successfully added to your shopping cart" not in modal_title.text:
            self.fail("The product was not successfully added to the cart.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()