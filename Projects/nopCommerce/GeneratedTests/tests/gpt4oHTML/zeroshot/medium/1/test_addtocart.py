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
        self.driver.get("http://max")  # Assume 'http://max' is the base URL

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the homepage
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.master-wrapper-page")))
        
        # Step 2: Click on the "Search" link in the top navigation
        search_link = driver.find_element(By.XPATH, "//a[text()='Search']")
        if not search_link:
            self.fail("Search link is not present")
        search_link.click()

        # Step 3: Enter "book" in the search field and submit the search
        wait.until(EC.presence_of_element_located((By.ID, "small-searchterms")))
        search_box = driver.find_element(By.ID, "small-searchterms")
        if not search_box:
            self.fail("Search box is not present")
        search_box.send_keys("book")
        
        search_button = driver.find_element(By.XPATH, "//button[contains(@class, 'search-box-button')]")
        if not search_button:
            self.fail("Search button is not present")
        search_button.click()

        # Step 4: On the search results page, locate the first product and click "Add to cart"
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.product-item")))
        add_to_cart_button = driver.find_element(By.XPATH, "(//button[contains(@class, 'product-box-add-to-cart-button')])[1]")
        if not add_to_cart_button:
            self.fail("Add to cart button for first product is not present")
        add_to_cart_button.click()

        # Step 5: Wait for the success notification to appear
        notification = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.bar-notification.success")))
        if not notification:
            self.fail("Success notification did not appear")

        # Step 6: Click the "shopping cart" link inside the notification
        cart_link = driver.find_element(By.XPATH, "//div[@class='bar-notification success']//a[text()='shopping cart']")
        if not cart_link:
            self.fail("Shopping cart link in notification is not present")
        cart_link.click()

        # Step 7: Confirm success by checking that the cart contains at least one item
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.shopping-cart-page")))
        cart_count = driver.find_elements(By.CSS_SELECTOR, "table.cart tbody tr")

        if not cart_count or len(cart_count) == 0:
            self.fail("The cart does not contain any items")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()