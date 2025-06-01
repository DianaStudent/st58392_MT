import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        # Set up Chrome driver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/en/")

    def test_add_to_cart(self):
        driver = self.driver

        # Open a product category from the top menu
        category_selector = (By.XPATH, "//ul[@id='top-menu']/li[@class='category']/a[contains(@href, 'http://localhost:8080/en/9-art')]")
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(category_selector)).click()

        # Select the first product listed in the category
        first_product_selector = (By.XPATH, "//div[contains(@class, 'js-product')][1]//a[contains(@class, 'product-thumbnail')]")
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(first_product_selector)).click()

        # On the product detail page, click the "Add to cart" button
        add_to_cart_button_selector = (By.XPATH, "//button[@class='btn btn-primary add-to-cart' and contains(., 'Add to cart')]")
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(add_to_cart_button_selector)).click()

        # Wait for the modal popup that confirms the product was added to the cart
        modal_selector = (By.XPATH, "//div[@id='blockcart-modal' and contains(@class, 'modal')]")
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(modal_selector))

        # Verify the modal contains a message like "Product successfully added to your shopping cart"
        modal_title_selector = (By.XPATH, "//div[@id='blockcart-modal']//h4[contains(text(), 'Product successfully added to your shopping cart')]")
        modal_title_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located(modal_title_selector))

        if not modal_title_element or not modal_title_element.text.strip():
            self.fail("Modal title not found or is empty.")

        # Assert the success message
        assert "Product successfully added to your shopping cart" in modal_title_element.text

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()