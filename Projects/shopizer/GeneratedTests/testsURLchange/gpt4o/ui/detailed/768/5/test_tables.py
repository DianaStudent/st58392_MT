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

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_visibility(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header is visible
        header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-area")))
        self.assertTrue(header.is_displayed())

        # Check footer is visible
        footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer-area")))
        self.assertTrue(footer.is_displayed())

        # Check navigation links are visible
        nav_links = ["Home", "Tables", "Chairs"]
        for link_text in nav_links:
            link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
            self.assertTrue(link.is_displayed())

        # Check login and register links
        login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
        self.assertTrue(login_link.is_displayed())

        register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
        self.assertTrue(register_link.is_displayed())

        # Check subscribe form is visible
        subscribe_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Your Email Address']")))
        self.assertTrue(subscribe_input.is_displayed())

        subscribe_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Subscribe']")))
        self.assertTrue(subscribe_button.is_displayed())

        # Check the presence and visibility of the first product's add to cart button
        add_to_cart_buttons = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[contains(@title, 'Add to cart')]")))
        if not add_to_cart_buttons:
            self.fail("Add to cart buttons are missing")
        
        for button in add_to_cart_buttons:
            self.assertTrue(button.is_displayed())

        # Check and click cookie consent button
        cookie_consent_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
        self.assertTrue(cookie_consent_button.is_displayed())
        
        # Click the button and ensure it visually affects the UI
        cookie_consent_button.click()

if __name__ == "__main__":
    unittest.main()