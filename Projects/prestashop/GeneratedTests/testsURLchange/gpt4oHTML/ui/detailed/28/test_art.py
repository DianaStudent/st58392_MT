import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIProcess(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Check visibility of header, footer, and navigation
        try:
            wait.until(EC.visibility_of_element_located((By.ID, "header")))
            wait.until(EC.visibility_of_element_located((By.ID, "footer")))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-nav")))
        except:
            self.fail("Header, Footer or Navigation not visible")

        # 2. Check presence and visibility of specific UI elements: input fields, buttons, labels, and sections

        # Check search input field
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='s']")))
        except:
            self.fail("Search input field is not visible")

        # Check buttons
        try:
            sign_in_button = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
            cart_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "i.shopping-cart")))
        except:
            self.fail("Buttons like sign-in or cart are not visible")

        # Check links
        try:
            clothes_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            accessories_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            art_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))
        except:
            self.fail("Navigation links like 'Clothes' or 'Accessories' are not visible")

        # 3. Interact with key UI elements (e.g., click buttons)
        try:
            sign_in_button.click()
            wait.until(EC.url_contains("login"))
            driver.back()
        except:
            self.fail("Failed to interact with the Sign in button")

        # 4. Confirm that the UI reacts visually
        try:
            search_input.click()
            search_input.send_keys("Art")
        except:
            self.fail("UI did not react on search input interaction")

        # 5. Assert that no required UI element is missing
        # Already checked in previous steps with self.fail() on exceptions

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()