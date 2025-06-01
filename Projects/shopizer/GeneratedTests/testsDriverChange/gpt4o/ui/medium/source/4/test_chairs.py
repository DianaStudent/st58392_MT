import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        
        # Check main navigation links
        home_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
        tables_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
        chairs_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
        
        # Check header elements
        logo = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".logo img")))
        self.assertTrue(logo.is_displayed(), "Logo not visible")
        
        # Check language selection
        language_selector = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".same-language-currency.language-style")))
        self.assertTrue(language_selector.is_displayed(), "Language selector not visible")

        # Check cart icon
        cart_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".icon-cart")))
        self.assertTrue(cart_icon.is_displayed(), "Cart icon not visible")
        
        # Check footer elements
        footer_logo = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".footer-logo img")))
        self.assertTrue(footer_logo.is_displayed(), "Footer logo not visible")

        # Interact with a button
        accept_cookies_button = self.wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
        accept_cookies_button.click()

        # Check that clicking does not cause errors
        self.assertTrue(home_link.is_displayed(), "Home link not visible after clicking button")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()