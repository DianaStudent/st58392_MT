import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8080/en/")

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to Art category
        try:
            art_category = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']"))
            )
            art_category.click()
        except:
            self.fail("Could not find or click the 'Art' category link.")

        # Click on the product "The best is yet to come' Framed poster"
        try:
            product = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='http://localhost:8080/en/art/3-13-the-best-is-yet-to-come-framed-poster.html#/19-dimension-40x60cm']"))
            )
            product.click()
        except:
            self.fail("Could not find or click the product link.")

        # Add the product to the cart
        try:
            add_to_cart_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary add-to-cart' and @type='submit']"))
            )
            add_to_cart_button.click()
        except:
            self.fail("Could not find or click the 'Add to cart' button.")

        # Wait for the modal to appear
        try:
            modal = wait.until(
                EC.visibility_of_element_located((By.ID, "blockcart-modal"))
            )
        except:
            self.fail("The modal did not appear after adding to cart.")

        # Verify the modal title
        try:
            modal_title = wait.until(
                EC.visibility_of_element_located((By.XPATH, "//h4[@class='modal-title h6 text-sm-center' and contains(text(), 'successfully added')]"))
            )
            self.assertTrue(modal_title.is_displayed(), "Modal title is not displayed.")
        except:
            self.fail("Could not find the success message in the modal.")

if __name__ == "__main__":
    unittest.main()