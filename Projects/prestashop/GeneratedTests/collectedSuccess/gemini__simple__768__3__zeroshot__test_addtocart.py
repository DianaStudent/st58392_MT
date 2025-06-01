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
        try:
            # Go to Art category
            art_category_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']"))
            )
            art_category_link.click()

            # Click on the product "The best is yet to come' Framed poster"
            product_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='http://localhost:8080/en/art/3-13-the-best-is-yet-to-come-framed-poster.html#/19-dimension-40x60cm']"))
            )
            product_link.click()

            # Add the product to the cart
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary add-to-cart']"))
            )
            add_to_cart_button.click()

            # Wait for the modal to appear
            modal = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "blockcart-modal"))
            )

            # Verify the modal title
            modal_title = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//h4[@class='modal-title h6 text-sm-center' and contains(text(), 'successfully added')]"))
            )
            self.assertTrue("successfully added" in modal_title.text)

        except Exception as e:
            self.fail(f"An error occurred: {e}")


if __name__ == "__main__":
    unittest.main()