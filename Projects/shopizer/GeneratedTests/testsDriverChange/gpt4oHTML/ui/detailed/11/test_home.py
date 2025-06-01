import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_ui_elements(self):
        driver = self.driver
        
        # Wait for the header to be visible
        header = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "header-area"))
        )
        if not header.is_displayed():
            self.fail("Header is not visible on the page.")
        
        # Check footer visibility
        footer = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "footer-area"))
        )
        if not footer.is_displayed():
            self.fail("Footer is not visible on the page.")

        # Check for navigation links
        nav_elements = [
            ("Home", "/"),
            ("Tables", "/category/tables"),
            ("Chairs", "/category/chairs"),
            ("Login", "/login"),
            ("Register", "/register"),
        ]
        for name, link in nav_elements:
            try:
                nav_link = driver.find_element(By.LINK_TEXT, name)
                self.assertTrue(nav_link.is_displayed(), f"{name} link is not visible.")
            except:
                self.fail(f"{name} link is not present on the page.")
        
        # Check presence and visibility of input fields and buttons
        try:
            subscribe_email_input = driver.find_element(By.NAME, "email")
            self.assertTrue(subscribe_email_input.is_displayed(), "Email input field is not visible.")
        except:
            self.fail("Email input field is missing.")

        try:
            subscribe_button = driver.find_element(By.CSS_SELECTOR, "button.button")
            self.assertTrue(subscribe_button.is_displayed(), "Subscribe button is not visible.")
        except:
            self.fail("Subscribe button is missing.")

        # Interact with a button and assert visible UI reaction
        try:
            accept_cookies_button = driver.find_element(By.ID, "rcc-confirm-button")
            accept_cookies_button.click()
            self.assertIn("display: none", accept_cookies_button.get_attribute("style"), "Cookie consent button did not disappear after clicking.")
        except:
            self.fail("Accept cookies button is missing or interaction failed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()