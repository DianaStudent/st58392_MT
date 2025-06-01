import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/")

    def test_add_to_cart(self):
        driver = self.driver

        # Wait for the search box to be present
        try:
            search_box = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "small-searchterms"))
            )
        except:
            self.fail("Search box is not present on home page.")

        # Enter search term and submit
        search_box.send_keys("book")
        try:
            search_button = driver.find_element(By.CLASS_NAME, "search-box-button")
            search_button.click()
        except:
            self.fail("Search button is not clickable.")

        # Wait for search results to be present
        try:
            product = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='product-item'][1]//button[contains(@class,'add-to-cart-button')]"))
            )
        except:
            self.fail("Product add-to-cart button is not present.")

        # Click on 'Add to cart' for the first product
        product.click()

        # Wait for the bar notification to confirm product addition
        try:
            success_notification = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "bar-notification"))
            )
            notification_text = success_notification.find_element(By.CLASS_NAME, "content").text
            self.assertIn("The product has been added to your shopping cart", notification_text)
        except:
            self.fail("Success notification is not visible or text does not match.")

        # Confirm cart has at least one item
        try:
            cart_count = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='mini-shopping-cart']//a"))
            )
            self.assertIn("1 item(s)", cart_count.text)
        except:
            self.fail("Cart does not contain at least one item.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()