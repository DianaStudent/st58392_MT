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
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver

        # 1. Click on the "Search" link in the top navigation.
        search_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Search"))
        )
        search_link.click()

        # 2. Enter "book" in the search field and submit the search.
        search_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "q"))
        )
        search_field.send_keys("book")

        search_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "button-1.search-button"))
        )
        search_button.click()

        # 3. On the search results page, locate the first product and click "Add to cart".
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "button-2.product-box-add-to-cart-button"))
        )
        add_to_cart_button.click()

        # 4. Wait for the success notification to appear.
        success_notification = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "bar-notification"))
        )

        # Check if the success notification is visible
        if not success_notification.is_displayed():
            self.fail("Success notification is not displayed.")

        # 5. Click the "shopping cart" link inside the notification.
        shopping_cart_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='bar-notification']//a[text()='shopping cart']"))
        )
        shopping_cart_link.click()

        # 6. Confirm success by checking that the cart page contains the added product.
        cart_table = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cart"))
        )

        # Check if the cart table is present
        if not cart_table:
            self.fail("Cart table is not found on the cart page.")

        # Check if there is at least one item in the cart
        cart_items = driver.find_elements(By.XPATH, "//table[@class='cart']/tbody/tr")
        if not cart_items:
            self.fail("No items found in the cart.")


if __name__ == "__main__":
    unittest.main()