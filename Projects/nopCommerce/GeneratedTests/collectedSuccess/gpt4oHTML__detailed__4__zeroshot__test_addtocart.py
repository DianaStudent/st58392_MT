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
        self.driver.get("http://max/")  # Placeholder for the actual store URL

    def test_add_to_cart_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to homepage and click on "Search"
        try:
            search_link = wait.until(EC.presence_of_element_located((By.XPATH, "//li/a[@href='/search']")))
        except Exception as e:
            self.fail(f"Search link not found: {e}")

        search_link.click()

        # Type "book" into the search field and submit
        try:
            search_input = wait.until(EC.presence_of_element_located(
                (By.ID, "small-searchterms")
            ))
            search_input.clear()
            search_input.send_keys("book")

            search_button = driver.find_element(By.XPATH, "//button[@class='button-1 search-box-button']")
            if not search_button:
                self.fail("Search button not found")
            search_button.click()
        except Exception as e:
            self.fail(f"Search input or button problem: {e}")

        # Wait for the product grid to load and locate the first result
        try:
            first_product_add_to_cart_button = wait.until(EC.presence_of_element_located(
                (By.XPATH, "(//button[@class='button-2 product-box-add-to-cart-button'])[1]")
            ))
            first_product_add_to_cart_button.click()
        except Exception as e:
            self.fail(f"First product's add to cart button not found: {e}")

        # Wait for the notification that the product is added to the cart
        try:
            notification_bar = wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//div[@class='bar-notification success']")
            ))
            self.assertTrue("The product has been added to your shopping cart" in notification_bar.text)

            cart_link = driver.find_element(By.XPATH, "//div[@class='bar-notification success']//a[@href='/cart']")
            if not cart_link:
                self.fail("Shopping cart link not found in notification")
            cart_link.click()
        except Exception as e:
            self.fail(f"Notification bar issue: {e}")

        # On the cart page, verify the correct product is present
        try:
            cart_item = wait.until(EC.presence_of_element_located(
                (By.XPATH, "//table[@class='cart']//tr/td[@class='product']//a[@class='product-name'][text()='Book1']")
            ))
            self.assertIsNotNone(cart_item, "Expected product not found in cart")
        except Exception as e:
            self.fail(f"Cart page product verification failed: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()