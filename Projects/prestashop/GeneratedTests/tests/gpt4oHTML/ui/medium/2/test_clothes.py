import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestWebInterface(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/3-clothes")

    def test_interface_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Check for main navigation links
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))

            # Check for sign in link
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))

            # Check for search input
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Search our catalog"]')))
            self.assertTrue(search_input.is_displayed())

            # Check for cart button
            cart_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'i.material-icons.shopping-cart')))
            self.assertTrue(cart_button.is_displayed())

            # Check for language selector
            language_selector = wait.until(EC.visibility_of_element_located((By.ID, 'language-selector-label')))
            self.assertTrue(language_selector.is_displayed())

            # Interact with elements
            # Click on the 'Sign in' link to ensure it redirects correctly
            sign_in_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in")))
            sign_in_link.click()
            wait.until(EC.url_contains("login"))

        except Exception as e:
            self.fail(f"Test failed due to missing or non-interactive element: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()