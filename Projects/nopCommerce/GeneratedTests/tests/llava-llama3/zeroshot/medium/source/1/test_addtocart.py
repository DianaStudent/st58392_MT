```
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.server import ServerManager
from selenium.webdriver import ActionChains

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().get_chromedriver())

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        driver.get("http://max/")

        # Locate the search input field and submit the query "book"
        search_input_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[contains(@name,'search')]"))))
        search_input_field.send_keys("book")
        search_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Search')]"))))

        # Click on the "Search" button
        search_button.click()

        # Locate the first product and click "Add to cart"
        first_product = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'product')][1]")))
        add_to_cart_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add to cart')]"))))
        first_product.find_element_by_css_selector("a").click()
        add_to_cart_button.click()

        # Wait for the success notification to appear
        success_notification = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'notification')][1]"))))

        # Click on the "Shopping cart" link inside the notification
        shopping_cart_link = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text,'shopping cart')]")))
        shopping_cart_link.click()

        # Confirm success by checking that the cart page contains the added product
        cart_page = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//table[contains(@class,'cart')][1]")))
        self.assertTrue(cart_page.find_elements_by_css_selector("tr"), "Cart should have at least one item.")

if __name__ == '__main__':
    unittest.main()
```