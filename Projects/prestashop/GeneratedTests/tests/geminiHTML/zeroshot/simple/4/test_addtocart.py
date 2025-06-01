import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


class AddToCartTest(unittest.TestCase):

    def setUp(self):
        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8080/en/")

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Go to Art category page
        try:
            art_category_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']"))
            )
            art_category_link.click()
        except Exception as e:
            self.fail(f"Could not navigate to Art category: {e}")

        # Click on the product "The best is yet to come' Framed poster"
        try:
            product_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='http://localhost:8080/en/art/3-13-the-best-is-yet-to-come-framed-poster.html#/19-dimension-40x60cm']"))
            )
            product_link.click()
        except Exception as e:
            self.fail(f"Could not navigate to product page: {e}")

        # Select dimension
        try:
            dimension_select = wait.until(
                EC.element_to_be_clickable((By.ID, "group_3"))
            )
            dimension_select.click()

            dimension_option = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//select[@id='group_3']/option[@value='19']"))
            )
            dimension_option.click()
        except Exception as e:
            self.fail(f"Could not select dimension: {e}")

        # Add to cart
        try:
            add_to_cart_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary add-to-cart']"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Could not add to cart: {e}")

        # Verify modal presence and success message
        try:
            modal = wait.until(
                EC.visibility_of_element_located((By.ID, "blockcart-modal"))
            )
            modal_title = wait.until(
                EC.visibility_of_element_located((By.XPATH, "//h4[@class='modal-title h6 text-sm-center' and contains(text(), 'successfully added')]"))
            )
            self.assertTrue("successfully added" in modal_title.text)
        except Exception as e:
            self.fail(f"Add to cart modal verification failed: {e}")


if __name__ == "__main__":
    unittest.main()