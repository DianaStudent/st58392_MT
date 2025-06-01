import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestAddToCart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")

    def test_add_to_cart(self):
        # Search for a book using the search box and submit the search
        search_box = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "search-box"))
        )
        search_box.send_keys("book")
        search_button = self.driver.find_element_by_css_selector("button[type='submit']")
        search_button.click()

        # Verify success notification is visible and contains a link to the cart
        success_notification = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, "success-notification"))
        )
        self.assertIn("Your book has been added to your cart", success_notification.text)
        cart_link = success_notification.find_element_by_css_selector("a[href='/cart']")
        cart_link.click()

        # Confirm cart contains at least one item
        cart_items = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".cart-item"))
        )
        self.assertGreater(len(cart_items), 0)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()