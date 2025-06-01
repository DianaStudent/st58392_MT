import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestSearchBook(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_search_book(self):
        self.driver.get("http://example.com")  # Assuming the website URL

        # Search for a book
        search_box = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "searchQuery"))
        )
        search_box.send_keys("Python")

        submit_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.NAME, "submit-search"))
        )
        submit_button.click()

        # Check success notification
        success_notification = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "success-notification"))
        )

        self.assertIn("Success!", success_notification.text)
        self.assertIn("Add to Cart", success_notification.text)

        # Click on the link in the success notification
        cart_link = WebDriverWait(success_notification.find_element(By.TAG_NAME, "a"), 20).get_attribute("href")
        cart_link_element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='" + cart_link + "']"))
        )
        cart_link_element.click()

        # Check that the cart contains at least one item
        cart_contents = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='cart-contents']/p"))
        )

        self.assertGreater(len(cart_contents), 0)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()