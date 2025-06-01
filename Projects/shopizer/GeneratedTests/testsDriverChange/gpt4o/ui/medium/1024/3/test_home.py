import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestWebsiteUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        try:
            # Verify navigation links
            home_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            tables_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            chairs_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
            login_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
            register_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))

            # Verify banner
            banner_img = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img[alt='banner']")))

            # Verify buttons
            accept_cookies_button = self.wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            subscribe_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".button")))

            # Interact with button and verify UI updates
            accept_cookies_button.click()
            self.wait.until(EC.invisibility_of_element((By.CLASS_NAME, "CookieConsent")))

            # Interact with subscribe email input
            subscribe_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.email")))
            subscribe_input.send_keys("test@example.com")

            # Assert no errors caused in the UI after interactions
            assert "No items added to cart" in self.driver.page_source

        except Exception as e:
            self.fail(f"Test failed due to missing UI element or unexpected error: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()