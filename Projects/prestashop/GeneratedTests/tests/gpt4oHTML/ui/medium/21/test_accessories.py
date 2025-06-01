import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestWebUI(unittest.TestCase):
    def setUp(self):
        # Setting up the Chrome WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/6-accessories")

    def test_main_ui_elements(self):
        driver = self.driver

        # Navigation links
        nav_links = [
            "http://localhost:8080/en/",
            "http://localhost:8080/en/3-clothes",
            "http://localhost:8080/en/6-accessories",
            "http://localhost:8080/en/9-art",
            "http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art",
            "http://localhost:8080/en/registration"
        ]

        # Check all navigation links are present and visible
        for link in nav_links:
            try:
                element = WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.XPATH, f"//a[@href='{link}']"))
                )
            except:
                self.fail(f"Navigation link {link} is missing or not visible.")

        # Check for other main UI components
        try:
            # Input fields (search)
            search_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "s"))
            )
            # Buttons (e.g., Cart)
            cart_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart"))
            )
            # Headers or any specific banners (main banner in header)
            header_banner = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "header"))
            )
        except:
            self.fail("A main UI component is missing or not visible.")

        # Interaction with an element: Click on a language selection dropdown
        try:
            language_dropdown = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".language-selector button"))
            )
            language_dropdown.click()

            # Ensure language dropdown options are displayed
            english_option = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//li/a[@data-iso-code='en']"))
            )
            latvia_option = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//li/a[@data-iso-code='lv']"))
            )
        except:
            self.fail("Language selection dropdown interaction failed or caused UI error.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()