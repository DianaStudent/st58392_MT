import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestUIProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check visibility of header, footer, and main navigation
        header = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "header.header-area")))
        self.assertTrue(header.is_displayed(), "Header is not visible")
        
        footer = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "footer.footer-area")))
        self.assertTrue(footer.is_displayed(), "Footer is not visible")
        
        main_navigation = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.main-menu nav")))
        self.assertTrue(main_navigation.is_displayed(), "Main navigation is not visible")
        
        # Check presence of elements
        # Check navigation links
        nav_links = main_navigation.find_elements(By.TAG_NAME, 'a')
        self.assertGreaterEqual(len(nav_links), 3, "Not all navigation links are present")

        # Check presence of buttons
        accept_cookies_button = self.wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
        self.assertTrue(accept_cookies_button.is_displayed(), "Accept cookies button is not visible")

        add_to_cart_buttons = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button[title='Add to cart']")))
        self.assertGreaterEqual(len(add_to_cart_buttons), 4, "Add to cart buttons are missing or not displayed correctly")

        # Check visibility and interaction with input fields, buttons
        email_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='email']")))
        self.assertTrue(email_input.is_displayed(), "Email input field is not visible")

        subscribe_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.button")))
        self.assertTrue(subscribe_button.is_displayed(), "Subscribe button is not visible")

        # Interact with accept cookies button
        accept_cookies_button.click()

        # Confirm reaction of UI
        confirm_cookies = driver.execute_script("return window.confirmationAccepted;")
        self.assertTrue(confirm_cookies, "Confirmation acceptance did not set correctly in UI")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()