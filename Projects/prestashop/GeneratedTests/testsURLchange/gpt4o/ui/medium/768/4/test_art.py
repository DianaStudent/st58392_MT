import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class ArtPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/9-art")
        self.wait = WebDriverWait(self.driver, 20)

    def test_key_ui_elements(self):
        driver = self.driver

        # Check for main navigation links
        try:
            home_link = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="http://localhost:8080/en/"]'))
            )
            clothes_link = driver.find_element(By.CSS_SELECTOR, 'a[href="http://localhost:8080/en/3-clothes"]')
            accessories_link = driver.find_element(By.CSS_SELECTOR, 'a[href="http://localhost:8080/en/6-accessories"]')
            art_link = driver.find_element(By.CSS_SELECTOR, 'a[href="http://localhost:8080/en/9-art"]')
            login_link = driver.find_element(By.CSS_SELECTOR, 'a[href="http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art"]')
            register_link = driver.find_element(By.CSS_SELECTOR, 'a[href="http://localhost:8080/en/registration"]')
        except Exception as e:
            self.fail(f"Navigation links are missing or not visible: {str(e)}")

        # Check for search input and 'Sign in' button
        try:
            search_input = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Search our catalog"]'))
            )
            sign_in_button = driver.find_element(By.CSS_SELECTOR, 'a[href="http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art"]')
        except Exception as e:
            self.fail(f"'Search our catalog' input or 'Sign in' button is missing: {str(e)}")

        # Check for category banner
        try:
            category_banner = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.block-category'))
            )
        except Exception as e:
            self.fail(f"Category banner is missing or not visible: {str(e)}")

        # Interact with the search input
        try:
            search_input.click()
            search_input.send_keys("poster")
            search_input.submit()
        except Exception as e:
            self.fail(f"Interaction with search input failed: {str(e)}")

        # Check search results have loaded
        try:
            results_header = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.total-products'))
            )
        except Exception as e:
            self.fail(f"Search results failed to load: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()