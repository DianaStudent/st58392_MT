from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestWebElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost/")

    def test_ui_elements(self):
        driver = self.driver

        # Elements to check
        elements = {
            "header": "header.header-area",
            "footer": "footer.footer-area",
            "nav_home": "a[href='/']",
            "nav_tables": "a[href='/category/tables']",
            "nav_chairs": "a[href='/category/chairs']",
            "login_link": "a[href='/login']",
            "register_link": "a[href='/register']",
            "cookie_consent": "div.CookieConsent",
            "accept_cookies_button": "button#rcc-confirm-button",
            "banner_shop_now": "a.btn.btn-black.rounded-0",
            "subscribe_email": "input[name='email']",
            "subscribe_button": "button.button"
        }

        # Check presence and visibility
        wait = WebDriverWait(driver, 20)
        for element_name, selector in elements.items():
            try:
                element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
                self.assertTrue(element.is_displayed(), f"{element_name} is not visible.")
            except:
                self.fail(f"{element_name} is missing or not visible.")

        # Interact with key UI elements
        try:
            accept_cookies = driver.find_element(By.CSS_SELECTOR, elements["accept_cookies_button"])
            accept_cookies.click()
            banner_button = driver.find_element(By.CSS_SELECTOR, elements["banner_shop_now"])
            banner_button.click()
        except Exception as e:
            self.fail(f"Interaction failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()