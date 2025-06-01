import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_components(self):
        driver = self.driver
        wait = self.wait
        
        # Verify main components exist on the homepage
        try:
            # Check header logo
            logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.logo > a > img")))
            self.assertTrue(logo.is_displayed(), "Logo is not visible")

            # Check navigation links
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            self.assertTrue(home_link.is_displayed(), "Home link is not visible")

            tables_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            self.assertTrue(tables_link.is_displayed(), "Tables link is not visible")

            chairs_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
            self.assertTrue(chairs_link.is_displayed(), "Chairs link is not visible")

            login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
            self.assertTrue(login_link.is_displayed(), "Login link is not visible")

            register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
            self.assertTrue(register_link.is_displayed(), "Register link is not visible")

            # Check Cart icon visibility
            cart_icon = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.icon-cart")))
            self.assertTrue(cart_icon.is_displayed(), "Cart icon is not visible")

            # Check footer elements
            footer_logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.footer-logo > a > img")))
            self.assertTrue(footer_logo.is_displayed(), "Footer logo is not visible")

            footer_links = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.footer-list > ul > li > a")))
            self.assertGreaterEqual(len(footer_links), 1, "No footer links found")

            # Check presence of Subscribe form
            email_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.email")))
            self.assertTrue(email_input.is_displayed(), "Email input is not visible")

            subscribe_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.button")))
            self.assertTrue(subscribe_button.is_displayed(), "Subscribe button is not visible")
        
        except Exception as e:
            self.fail(f"UI component test failed due to: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()