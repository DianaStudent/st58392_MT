import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_present_and_visible(self):
        driver = self.driver

        try:
            # Wait until header is visible
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area")))
            
            # Check the main menu elements
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))

            # Ensure footer is present
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer.footer-area")))

            # Check Cookie Consent banner
            cookie_consent = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "CookieConsent")))
            accept_button = cookie_consent.find_element(By.ID, "rcc-confirm-button")
            self.assertTrue(accept_button.is_displayed(), "Accept cookies button not visible")
            accept_button.click()

            # Verify input fields are present
            subscribe_input = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.email")))
            self.assertTrue(subscribe_input.is_displayed(), "Subscribe input is not visible")

            # Check product sections
            featured_products = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.product-area")))
            self.assertTrue(featured_products.is_displayed(), "Featured Products section is not visible")

            # Check buttons like 'Shop Now'
            shop_now_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "Shop Now")))
            self.assertTrue(shop_now_button.is_displayed(), "'Shop Now' button is not visible")
            shop_now_button.click()

            # Ensure header elements react visually
            login_link = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
            self.assertTrue(login_link.is_displayed(), "Login link is not visible")

            register_link = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
            self.assertTrue(register_link.is_displayed(), "Register link is not visible")

        except Exception as e:
            self.fail(f'UI Test Failed: {str(e)}')

if __name__ == "__main__":
    unittest.main()