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
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to Art category
        try:
            art_category = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='Art']"))
            )
            art_category.click()
        except:
            self.fail("Could not find or click Art category link.")

        # Click on the product "The best is yet to come' Framed poster"
        try:
            product_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()=\"The best is yet to come'...\"]"))
            )
            product_link.click()
        except:
            self.fail("Could not find or click the product link.")

        # Select the dimension
        try:
            dimension_select = wait.until(
                EC.element_to_be_clickable((By.ID, "group_3"))
            )
            dimension_select.click()
        except:
            self.fail("Could not find or click the dimension select.")

        # Add the product to the cart
        try:
            add_to_cart_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'add-to-cart')]"))
            )
            add_to_cart_button.click()
        except:
            self.fail("Could not find or click the Add to cart button.")

        # Verify the modal confirmation
        try:
            modal_title = wait.until(
                EC.visibility_of_element_located((By.XPATH, "//h4[@class='modal-title h6 text-sm-center' and contains(text(), 'successfully added')]"))
            )
            self.assertTrue(modal_title.is_displayed(), "Modal title is not displayed.")
        except:
            self.fail("Modal confirmation title not found or not displayed.")

if __name__ == "__main__":
    unittest.main()