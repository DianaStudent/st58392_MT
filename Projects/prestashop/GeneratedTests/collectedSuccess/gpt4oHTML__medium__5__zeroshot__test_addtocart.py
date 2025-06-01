import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_add_to_cart(self):
        driver = self.driver

        # Step 1: Open the home page
        driver.get("http://localhost:8080/en/")
        wait = WebDriverWait(driver, 20)

        # Step 2: Click on a product category (e.g. 'Art' from the top menu)
        try:
            art_category = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Art')]")))
            art_category.click()
        except:
            self.fail("Art category not found or not clickable")

        # Step 3: Select the first product listed in the category
        try:
            first_product = wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//div[@id='js-product-list']/div[@class='products row']/div[1]//a[@class='thumbnail product-thumbnail']")))
            first_product.click()
        except:
            self.fail("First product not found or not clickable")

        # Step 4: On the product detail page, click the "Add to cart" button
        try:
            add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "add-to-cart")))
            add_to_cart_button.click()
        except:
            self.fail("Add to cart button not found or not clickable")

        # Step 5: Wait for the modal popup that confirms the product was added to the cart
        try:
            modal = wait.until(EC.visibility_of_element_located((By.ID, "blockcart-modal")))
        except:
            self.fail("Modal confirming product addition to cart did not appear")

        # Step 6: Verify the modal contains a message like "Product successfully added to your shopping cart"
        try:
            modal_message = modal.find_element(By.CLASS_NAME, "modal-title").text
            self.assertIn("successfully added", modal_message.lower(), "Success message not found in modal")
        except:
            self.fail("Modal title with success message not found")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()