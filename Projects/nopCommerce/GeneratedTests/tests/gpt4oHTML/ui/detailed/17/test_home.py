import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        
        # Ensure header, footer, and navigation are visible
        header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header')))
        footer = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'footer')))
        navigation = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header-menu')))

        # Check the presence and visibility of input fields, buttons, and links
        search_box = self.wait.until(EC.visibility_of_element_located((By.ID, 'small-searchterms')))
        search_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.button-1.search-box-button')))
        register_link = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.ico-register')))
        login_link = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.ico-login')))
        cart = self.wait.until(EC.visibility_of_element_located((By.ID, 'topcartlink')))
        newsletter_input = self.wait.until(EC.visibility_of_element_located((By.ID, 'newsletter-email')))
        subscribe_button = self.wait.until(EC.visibility_of_element_located((By.ID, 'newsletter-subscribe-button')))

        # Interactions and UI reactions
        register_link.click()
        self.wait.until(EC.url_contains("/register?returnUrl=%2F"))
        self.driver.back()

        login_link.click()
        self.wait.until(EC.url_contains("/login?returnUrl=%2F"))
        self.driver.back()

        search_box.send_keys("test search")
        search_button.click()
        self.wait.until(EC.url_contains("/search?q=test%20search"))

        newsletter_input.send_keys("test@example.com")
        subscribe_button.click()

        # Confirm that all required elements are present and visible
        elements = [header, footer, navigation, search_box, search_button, 
                    register_link, login_link, cart, newsletter_input, subscribe_button]
        for element in elements:
            if not element.is_displayed():
                self.fail(f"Element {element} is not displayed as expected.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()