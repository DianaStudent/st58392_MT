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
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait

        # Navigate to the homepage and click on "Search"
        search_menu = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='header-menu']//a[text()='Search']")))
        self.assertTrue(search_menu)
        search_menu.click()

        # Type the search term "book" into the search field
        search_box = wait.until(EC.presence_of_element_located((By.ID, "q")))
        self.assertTrue(search_box)
        search_box.send_keys("book")

        # Submit the search
        search_button = driver.find_element(By.XPATH, "//button[@class='button-1 search-button']")
        self.assertTrue(search_button)
        search_button.click()

        # Wait for the product grid to load
        product_grid = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-grid")))
        self.assertTrue(product_grid)

        # Locate the first product result and click the "Add to cart" button
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='item-box']//button[@class='button-2 product-box-add-to-cart-button']")))
        self.assertTrue(add_to_cart_button)
        add_to_cart_button.click()

        # Wait for the notification bar to appear
        notification = wait.until(EC.visibility_of_element_located((By.ID, "bar-notification")))
        self.assertTrue(notification)

        # Ensure the notification contains a link to the cart
        cart_link = driver.find_element(By.XPATH, "//div[@class='bar-notification success']//a[@href='/cart']")
        self.assertTrue(cart_link)

        # Click the "shopping cart" link
        cart_link.click()

        # On the cart page, verify that the expected product is present
        cart_page = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping-cart-page")))
        self.assertTrue(cart_page)
        
        product_in_cart = driver.find_element(By.XPATH, "//table[@class='cart']//td[@class='product']//a[text()='Book1']")
        self.assertTrue(product_in_cart)

        cart_item_count = driver.find_element(By.XPATH, "//div[@class='count']//a[contains(text(),'item(s)')]")
        self.assertTrue(cart_item_count)
        self.assertNotEqual(cart_item_count.text, "There are no item(s) in your cart.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()