from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class WebsiteUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def test_UI_elements(self):
        driver = self.driver

        # Wait for header to be present and visible
        header = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "header"))
        )
        self.assertTrue(header.is_displayed(), "Header is not visible")

        # Verify the presence of navigation links
        nav_links = [
            ("Clothes", "http://localhost:8080/en/3-clothes"),
            ("Accessories", "http://localhost:8080/en/6-accessories"),
            ("Art", "http://localhost:8080/en/9-art"),
            ("Sign in", "http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F"),
            ("Register", "http://localhost:8080/en/registration"),
        ]

        for link_text, url in nav_links:
            link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, link_text))
            )
            self.assertTrue(link.is_displayed(), f"Link '{link_text}' is not visible")
            self.assertEqual(link.get_attribute("href"), url, f"Link '{link_text}' URL is incorrect")

        # Verify the presence of input field for search
        search_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Search our catalog']"))
        )
        self.assertTrue(search_input.is_displayed(), "Search input is not visible")

        # Verify the presence of a button
        cart_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart"))
        )
        self.assertTrue(cart_button.is_displayed(), "Cart button is not visible")

        # Interact with elements - example: click the language selector
        language_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".language-selector button"))
        )
        language_button.click()

        # Confirm dropdown is visible
        dropdown_menu = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".dropdown-menu"))
        )
        self.assertTrue(dropdown_menu.is_displayed(), "Language dropdown is not visible after clicking")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()