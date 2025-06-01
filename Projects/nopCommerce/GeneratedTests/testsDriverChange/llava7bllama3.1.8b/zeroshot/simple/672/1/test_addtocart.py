from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium.webdriver.chrome.service import Service as ChromeService

class TestAddToCartSimple(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")

    def test_add_to_cart_simple(self):
        # Search for a book using the search box and submit the search.
        search_box = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "q")))
        search_box.send_keys("book")
        search_button = self.driver.find_element_by_name("submit")
        search_button.click()

        # The success notification must be visible and contain a link to the cart.
        success_notification = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "success-msg")))
        success_link = success_notification.find_element_by_tag_name("a")

        # Confirm success by checking that the cart contains at least one item.
        cart_link = self.driver.find_element_by_name("cart")
        cart_link.click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "cart_contents")))
        items_in_cart = self.driver.find_elements_by_css_selector("#cart_contents li")

        # Check if any required element is missing.
        self.assertGreater(len(items_in_cart), 0)
        self.failUnless(success_notification.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()