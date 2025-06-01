from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the home page. (Done in setUp)

        # 2. Click on a product category (e.g. from the top menu).
        try:
            category_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//ul[@id='top-menu']/li[@id='category-9']/a"))
            )
            category_link.click()
        except Exception as e:
            self.fail(f"Could not click on category link: {e}")

        # 3. Select the first product listed in the category.
        try:
            first_product = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[@id='js-product-list']/div[@class='products row']/div[1]//a[@class='thumbnail product-thumbnail']"))
            )
            first_product.click()
        except Exception as e:
            self.fail(f"Could not click on first product: {e}")

        # 4. On the product detail page, click the "Add to cart" button.
        try:
            add_to_cart_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".add-to-cart"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Could not click on add to cart button: {e}")

        # 5. Wait for the modal popup that confirms the product was added to the cart.
        try:
            modal = wait.until(
                EC.visibility_of_element_located((By.ID, "blockcart-modal"))
            )
        except Exception as e:
            self.fail(f"Modal did not appear: {e}")

        # 6. Verify the modal contains a message like "Product successfully added to your shopping cart".
        try:
            modal_title_element = wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "modal-title"))
            )

            if modal_title_element:
                modal_title_text = modal_title_element.text
                if modal_title_text and "successfully added to your shopping cart" in modal_title_text:
                    pass  # Success!
                else:
                    self.fail(f"Modal title text is incorrect: {modal_title_text}")
            else:
                self.fail("Modal title element not found.")
        except Exception as e:
            self.fail(f"Could not verify modal title: {e}")


if __name__ == "__main__":
    unittest.main()