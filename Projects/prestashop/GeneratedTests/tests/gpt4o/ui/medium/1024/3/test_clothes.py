import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestClothesPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/3-clothes")
        self.driver.maximize_window()

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Confirm presence of key interface elements
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
            self.assertIsNotNone(header, "Header is not visible.")

            nav_links = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".top-menu .category a")))
            self.assertGreater(len(nav_links), 0, "Navigation links are missing or not visible.")

            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[aria-label='Search']")))
            self.assertIsNotNone(search_input, "Search input is not visible.")

            # Check buttons
            cart_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart")))
            self.assertIsNotNone(cart_button, "Cart button is not visible.")

            sign_in_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[title='Log in to your customer account']")))
            self.assertIsNotNone(sign_in_button, "Sign in button is not visible.")

            # Interact with search input
            search_input.click()
            search_input.send_keys("T-shirt")

            submit_search = driver.find_element_by_css_selector("button[type='submit']")
            submit_search.click()

            # Verify interaction did not cause errors
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#js-product-list")))

        except Exception as e:
            self.fail(f"Test failed due to: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()