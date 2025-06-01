```
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import Until
from selenium.webdriver.support import expected_conditions as EC

class TestBookSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20, "time.sleep")

    def tearDown(self):
        self.driver.quit()

    def test_book_search(self):
        self.driver.get("https://example.com/")
        search_link = self.driver.find_element_by_tag_name("a").get_attribute("href")
        self.assertEqual(search_link, "https://example.com/search?search_type=basic&cat_id=1&search_item=&order_column=priority")

        search_field = self.driver.find_element_by_name("search_item")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text()='Search')]")))
        search_button = self.driver.find_element_by_name("search_type")
        self.assertEqual(searchbutton.get_attribute("value"), "basic")

        product_link = WebDriverWait(self.driver, 20).until(EC.element_located((By.XPATH, "//a[contains(@href, 'product/12345')]")))
        product_link.click()

        cart_button = WebDriverWait(self.driver, 20).until(EC.element_located((By.XPATH, "//button[contains(@data-cart-count,'1')]")))
        cart_button.click()
        
        success_notification = self.driver.find_element_by_css_selector("div[role='alert']")
        cart_link = self.driver.find_element_by_css_selector("a.cart-link")
        self.assertTrue(success_notification.get_attribute("role") == "alert", "Success notification is not a role of alert.")
        self.assertTrue(cart_link.get_attribute("class") == "cart-link", "Cart link has wrong class attribute.")

if __name__ == '__main__':
    unittest.main()
```