import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestCartPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")

    def test_home_page_elements(self):
        # Check navigation links
        nav_links = WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "ul.nav li a")))
        self.assertGreater(len(nav_links), 0)

        # Check inputs and buttons
        inputs_and_buttons = WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".form-control, button")))
        self.assertGreater(len(inputs_and_buttons), 0)

        # Check banners
        banner = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".banner")))
        self.assertIsNotNone(banner.text)

    def test_interactive_elements(self):
        # Click a button and check that the UI updates visually
        search_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        search_button.click()

        # Verify that interactive elements do not cause errors in the UI
        error_message = WebDriverWait(self.driver, 20).until_not(EC.presence_of_element_located((By.CSS_SELECTOR, ".error-message")))
        self.assertIsNotNone(error_message)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()