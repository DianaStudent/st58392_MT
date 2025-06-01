import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestSearchBook(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_search_book(self):
        # Navigate to the webpage
        self.driver.get("your_url")

        # Search for a book using the search box and submit the search
        search_box = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='search']")))
        search_box.send_keys("book_name")
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()

        # The success notification must be visible and contain a link to the cart
        notification = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".success-notification")))
        self.assertTrue(notification.text.startswith("Search Results for"))
        cart_link = self.driver.find_element(By.CSS_SELECTOR, "a[href='/cart']")
        self.assertEqual(cart_link.get_attribute("href"), "/cart")

        # Confirm success by checking that the cart contains at least one item
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-total")))
        self.assertGreater(int(self.driver.find_element(By.CSS_SELECTOR, "span.value-summary").text.replace("$", "")), 0)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()