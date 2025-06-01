import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AccessoriesPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/6-accessories")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_presence(self):
        try:
            # Check presence of header
            header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
            self.assertTrue(header.is_displayed(), "Header is not visible.")

            # Check presence of navigation links
            nav_links = self.driver.find_elements(By.CSS_SELECTOR, "a.dropdown-item")
            self.assertTrue(len(nav_links) > 0, "Navigation links are not present.")

            # Check presence of search input
            search_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='s']")))
            self.assertTrue(search_input.is_displayed(), "Search input is not visible.")

            # Check presence of buttons
            buttons = self.driver.find_elements(By.CSS_SELECTOR, "button")
            self.assertTrue(len(buttons) > 0, "Buttons are not present.")

            # Check presence of banner
            banners = self.driver.find_elements(By.CLASS_NAME, "header-banner")
            self.assertTrue(any(banner.is_displayed() for banner in banners), "Banners are not visible.")

            # Interact with an element
            cart_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "blockcart")))
            cart_button.click()

            # Verify UI updates: Check cart count
            cart_count = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "cart-products-count")))
            self.assertIn("(0)", cart_count.text, "Cart count did not update correctly after interaction.")

        except Exception as e:
            self.fail(f"UI elements are not present or interaction failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()