import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class UITest(unittest.TestCase):

    def setUp(self):
        # Setup Chrome WebDriver with WebDriver Manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/3-clothes")
        self.driver.set_window_size(1920, 1080)  # Optional: to ensure full visibility

    def test_ui_components(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Check for structural elements
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
            footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
            self.assertTrue(header.is_displayed(), "Header should be visible")
            self.assertTrue(footer.is_displayed(), "Footer should be visible")
        except Exception as e:
            self.fail(f"Required structural elements are missing or not visible: {e}")

        # Check for input fields, buttons, labels, and sections
        try:
            search_field = wait.until(EC.visibility_of_element_located((By.NAME, "s")))
            search_button = driver.find_element(By.CSS_SELECTOR, "i.material-icons.search")
            catalog_label = driver.find_element(By.XPATH, "//input[@name='s']/following-sibling::input")
            self.assertTrue(search_field.is_displayed(), "Search input field should be visible")
            self.assertTrue(search_button.is_displayed(), "Search button should be visible")
            self.assertTrue(catalog_label.is_displayed(), "Catalog label should be visible")
        except Exception as e:
            self.fail(f"Required UI components are missing or not visible: {e}")

        # Interact with key UI elements
        try:
            navigation_links = [
                ("Home", "http://localhost:8080/en/"),
                ("Clothes", "http://localhost:8080/en/3-clothes"),
                ("Accessories", "http://localhost:8080/en/6-accessories"),
                ("Art", "http://localhost:8080/en/9-art"),
            ]

            for link_text, expected_url in navigation_links:
                link = driver.find_element(By.LINK_TEXT, link_text)
                self.assertTrue(link.is_displayed(), f"Link {link_text} should be visible")
                link.click()
                wait.until(EC.url_to_be(expected_url))
                self.assertEqual(driver.current_url, expected_url, f"URL should be {expected_url}")
                driver.back()
        except Exception as e:
            self.fail(f"Failed to interact with UI elements and navigate: {e}")

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()