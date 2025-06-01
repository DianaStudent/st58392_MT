import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.url = "http://localhost:8080/en/"
        self.driver.get(self.url)

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
        except Exception as e:
            self.fail(f"Could not navigate to Art category: {e}")

        # Select the product 'The best is yet to come'
        try:
            product = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='http://localhost:8080/en/art/3-13-the-best-is-yet-to-come-framed-poster.html#/19-dimension-40x60cm']"))
            )
            product.click()
        except Exception as e:
            self.fail(f"Could not select product: {e}")

        # Add the product to the cart
        try:
            add_to_cart_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary add-to-cart']"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Could not add product to cart: {e}")

        # Verify the modal confirmation
        try:
            modal_title = wait.until(
                EC.visibility_of_element_located((By.XPATH, "//h4[@class='modal-title h6 text-sm-center' and contains(text(), 'successfully added')]"))
            )
            self.assertTrue(modal_title.is_displayed(), "Modal title is not displayed")
        except Exception as e:
            self.fail(f"Modal confirmation not found: {e}")


if __name__ == "__main__":
    unittest.main()