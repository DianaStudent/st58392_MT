import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestWebUI(unittest.TestCase):
    def setUp(self):
        # Set up the Chrome webdriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_ui_components(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Check header and logo
        try:
            logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".logo img")))
            self.assertTrue(logo.is_displayed(), "Logo is not displayed")
        except:
            self.fail("Logo element is missing or not visible.")

        # Check main menu links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            self.assertTrue(home_link.is_displayed(), "Home link is not displayed")

            tables_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            self.assertTrue(tables_link.is_displayed(), "Tables link is not displayed")

            chairs_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
            self.assertTrue(chairs_link.is_displayed(), "Chairs link is not displayed")
        except:
            self.fail("Main menu links are missing or not visible.")

        # Check Cookie consent button
        try:
            cookie_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            self.assertTrue(cookie_button.is_displayed(), "Cookie accept button is not displayed")
        except:
            self.fail("Cookie consent button is missing or not visible.")

        # Check account links
        try:
            account_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".account-setting-active")))
            self.assertTrue(account_button.is_displayed(), "Account button is not displayed")
            
            cart_icon = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".icon-cart")))
            self.assertTrue(cart_icon.is_displayed(), "Cart icon is not displayed")
        except:
            self.fail("Header account related elements are missing or not visible.")

        # Check footer links
        try:
            contact_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Contact")))
            self.assertTrue(contact_link.is_displayed(), "Contact link is not displayed")

            login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
            self.assertTrue(login_link.is_displayed(), "Login link is not displayed")

            register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
            self.assertTrue(register_link.is_displayed(), "Register link is not displayed")
        except:
            self.fail("Footer links are missing or not visible.")

    def tearDown(self):
        # Tear down the web driver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()