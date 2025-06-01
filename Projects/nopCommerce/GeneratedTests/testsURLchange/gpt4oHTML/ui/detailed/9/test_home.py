import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        try:
            # Structural elements
            header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
            footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
            self.assertTrue(header and footer, "Header or Footer is not visible.")

            # Input fields
            search_box = wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
            self.assertTrue(search_box, "Search box is not visible.")

            # Buttons
            search_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-box-button")))
            self.assertTrue(search_button, "Search button is not visible.")

            # Labels and sections
            cart_label = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "cart-label")))
            self.assertTrue(cart_label, "Cart label is not visible.")

            # Interact with elements
            search_box.send_keys("test")
            search_button.click()

            # Confirm UI reactions
            # Checking that search results page loads
            wait.until(EC.url_contains("search?q=test"))

            # Check for top menu
            top_menu = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "top-menu")))
            self.assertTrue(top_menu, "Top menu is not visible.")

        except Exception as e:
            self.fail(f"Test failed due to missing UI component: {e}")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()