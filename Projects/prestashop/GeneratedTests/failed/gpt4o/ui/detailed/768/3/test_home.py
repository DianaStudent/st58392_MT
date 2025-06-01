from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestDemoPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_ui_elements(self):
        driver = self.driver

        # Verify header is visible
        header = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "header"))
        )
        self.assertTrue(header.is_displayed(), "Header is not visible")

        # Verify footer is visible
        footer = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "footer"))
        )
        self.assertTrue(footer.is_displayed(), "Footer is not visible")

        # Verify navigation menu is visible
        top_menu = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "_desktop_top_menu"))
        )
        self.assertTrue(top_menu.is_displayed(), "Navigation menu is not visible")

        # Verify search input field is visible
        search_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.NAME, "s"))
        )
        self.assertTrue(search_input.is_displayed(), "Search input field is not visible")
        
        # Verify the presence of buttons and click
        try:
            sign_in_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@title='Log in to your customer account']"))
            )
            sign_in_button.click()

            # Confirm that the UI reacts visually, check login page
            login_page = WebDriverWait(driver, 20).until(
                EC.title_contains("Login")
            )
        except Exception as e:
            self.fail(f"UI element interaction failed: {e}")
        
        # Assert that other key UI elements are present and visible
        for selector, description in [
            ("//a[@href='/en/3-clothes']", "Clothes category link"),
            ("//a[@href='/en/6-accessories']", "Accessories category link"),
            ("//a[@href='/en/9-art']", "Art category link"),
            ("//form[@method='post']", "Newsletter subscription form"),
        ]:
            element = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, selector))
            )
            self.assertTrue(element.is_displayed(), f"{description} is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()