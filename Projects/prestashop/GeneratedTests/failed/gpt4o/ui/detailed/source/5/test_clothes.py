from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestClothesPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/3-clothes")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Wait for header and check visibility
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
            self.assertTrue(header.is_displayed(), "Header is not visible")

            # Wait for footer and check visibility
            footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
            self.assertTrue(footer.is_displayed(), "Footer is not visible")

            # Check for main navigation links
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            self.assertTrue(home_link.is_displayed(), "Home link is not visible")

            clothes_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            self.assertTrue(clothes_link.is_displayed(), "Clothes link is not visible")

            # Check for input fields
            search_input = wait.until(EC.visibility_of_element_located((By.NAME, "s")))
            self.assertTrue(search_input.is_displayed(), "Search input is not visible")

            # Check for buttons
            sort_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".sort-by-row button")))
            self.assertTrue(sort_button.is_displayed(), "Sort by button is not visible")

            subscribe_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='submitNewsletter']")))
            self.assertTrue(subscribe_button.is_displayed(), "Subscribe button is not visible")

            # Interact with elements
            home_link.click()
            wait.until(EC.url_to_be("http://localhost:8080/en/"))

            # Assert that page title changed
            self.assertEqual(driver.title, "Home")

        except Exception as e:
            self.fail(f"Test failed due to missing or non-visible element: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()