import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddToCartTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

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
            self.fail(f"Could not click on Art category link: {e}")

        # Click on the product "The best is yet to come' Framed poster"
        try:
            product_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='http://localhost:8080/en/art/3-13-the-best-is-yet-to-come-framed-poster.html#/19-dimension-40x60cm']"))
            )
            product_link.click()
        except Exception as e:
            self.fail(f"Could not click on the product link: {e}")

        # Select the dimension
        try:
            dimension_select = wait.until(
                EC.element_to_be_clickable((By.ID, "group_3"))
            )
            dimension_select.click()
        except Exception as e:
            self.fail(f"Could not click on the dimension select: {e}")

        # Add the product to the cart
        try:
            add_to_cart_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary add-to-cart']"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Could not click on the add to cart button: {e}")

        # Wait for the modal to appear
        try:
            modal = wait.until(
                EC.visibility_of_element_located((By.ID, "blockcart-modal"))
            )
        except Exception as e:
            self.fail(f"Modal did not appear: {e}")

        # Verify the modal title
        try:
            modal_title = wait.until(
                EC.visibility_of_element_located((By.ID, "myModalLabel"))
            )
            self.assertIn("successfully added to your shopping cart", modal_title.text)
        except Exception as e:
            self.fail(f"Could not verify modal title: {e}")


if __name__ == "__main__":
    unittest.main()