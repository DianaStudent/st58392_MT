import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check for Cookie Consent button
        try:
            cookie_consent = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            self.assertTrue(cookie_consent.is_displayed())
        except:
            self.fail("Cookie Consent button is not visible")

        # Check for header logo
        try:
            header_logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.logo a img")))
            self.assertTrue(header_logo.is_displayed())
        except:
            self.fail("Header logo is not visible")

        # Check for main menu links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            tables_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            chairs_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
            self.assertTrue(home_link.is_displayed())
            self.assertTrue(tables_link.is_displayed())
            self.assertTrue(chairs_link.is_displayed())
        except:
            self.fail("One or more main menu links are not visible")

        # Check for account settings button on larger screens
        try:
            account_settings_btn = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "account-setting-active")))
            self.assertTrue(account_settings_btn.is_displayed())
        except:
            self.fail("Account settings button is not visible on larger screens")

        # Check for mobile cart icon on smaller screens
        try:
            cart_icon_mobile = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.same-style.cart-wrap.d-block.d-lg-none a.icon-cart")))
            self.assertTrue(cart_icon_mobile.is_displayed())
        except:
            self.fail("Cart icon for mobile view is not visible")

        # Check for login and register links
        try:
            login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
            register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
            self.assertTrue(login_link.is_displayed())
            self.assertTrue(register_link.is_displayed())
        except:
            self.fail("Login or Register links are not visible")

        # Check for footer elements
        try:
            footer_logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.footer-logo a img")))
            self.assertTrue(footer_logo.is_displayed())
        except:
            self.fail("Footer logo is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()