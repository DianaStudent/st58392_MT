import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestClothesPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/3-clothes")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_present_and_interactive(self):
        driver = self.driver
        wait = self.wait

        # Verify navigation links
        nav_links = [
            ("Home", By.XPATH, "//a[span='Home']"),
            ("Clothes", By.XPATH, "//li/span[text()='Clothes']"),
            ("Accessories", By.XPATH, "//a[text()='Accessories']"),
            ("Art", By.XPATH, "//a[text()='Art']")
        ]

        for name, by, value in nav_links:
            self.assertTrue(wait.until(EC.visibility_of_element_located((by, value))), f"{name} link is not visible")

        # Verify login and register links
        auth_links = [
            ("Sign in", By.XPATH, "//a/span[text()='Sign in']"),
            ("Create account", By.XPATH, "//a[text()='Create account']")
        ]

        for name, by, value in auth_links:
            self.assertTrue(wait.until(EC.visibility_of_element_located((by, value))), f"{name} link is not visible")

        # Verify search input
        search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[aria-label='Search']")))
        self.assertIsNotNone(search_input, "Search input is not visible")

        # Verify 'Filter By' and filtering options
        filter_by = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[text()='Filter By']")))
        self.assertIsNotNone(filter_by, "'Filter By' section is not visible")

        # Interact with a checkbox
        availability_checkbox = wait.until(EC.element_to_be_clickable((By.ID, "facet_input_2473_0")))
        availability_checkbox.click()
        
        # Check that filtering results in visible changes by verifying checkbox is checked
        self.assertTrue(availability_checkbox.is_selected(), "Checkbox did not update correctly after clicking")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()