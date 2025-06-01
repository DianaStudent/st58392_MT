import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class AccessoriesPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/6-accessories")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_accessories_page_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header elements
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
            self.assertTrue(header.is_displayed(), "Header is not visible")
        except Exception as e:
            self.fail(f"Header not found: {e}")

        # Check footer elements
        try:
            footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
            self.assertTrue(footer.is_displayed(), "Footer is not visible")
        except Exception as e:
            self.fail(f"Footer not found: {e}")

        # Check navigation menu
        for link_text in ["Home", "Clothes", "Accessories", "Art"]:
            try:
                nav_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
                self.assertTrue(nav_link.is_displayed(), f"Navigation link '{link_text}' is not visible")
            except Exception as e:
                self.fail(f"Navigation link '{link_text}' not found: {e}")

        # Check login button
        try:
            login_button = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
            self.assertTrue(login_button.is_displayed(), "Login button is not visible")
            # Interact
            login_button.click()
            self.assertEqual(driver.current_url, "http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F6-accessories")
            driver.back()
        except Exception as e:
            self.fail(f"Login button not found or interaction failed: {e}")

        # Check product list
        try:
            product_list = wait.until(EC.visibility_of_element_located((By.ID, "products")))
            self.assertTrue(product_list.is_displayed(), "Product list is not visible")
        except Exception as e:
            self.fail(f"Product list not found: {e}")

        # Check search input field
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#search_widget input[name='s']")))
            self.assertTrue(search_input.is_displayed(), "Search input field is not visible")
        except Exception as e:
            self.fail(f"Search input field not found: {e}")

        # Check button in the newsletter subscription
        try:
            subscribe_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='submitNewsletter']")))
            self.assertTrue(subscribe_button.is_displayed(), "Subscribe button is not visible")
        except Exception as e:
            self.fail(f"Subscribe button not found: {e}")

if __name__ == "__main__":
    unittest.main()