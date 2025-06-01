import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestWebElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_UI_elements(self):
        driver = self.driver

        # Check for the presence and visibility of key UI elements
        try:
            # Header navigation links
            nav_links = [
                (By.LINK_TEXT, "Home"),
                (By.LINK_TEXT, "Tables"),
                (By.LINK_TEXT, "Chairs")
            ]

            for link_text in nav_links:
                element = self.wait.until(EC.visibility_of_element_located(link_text))
                self.assertTrue(element.is_displayed(), f"{link_text[1]} link is not visible.")

            # Cookie consent button
            accept_cookies_btn = self.wait.until(
                EC.visibility_of_element_located((By.ID, "rcc-confirm-button"))
            )
            self.assertTrue(accept_cookies_btn.is_displayed(), "Accept cookies button is not visible.")
            # Click the button as part of interaction
            accept_cookies_btn.click()

            # 'Shop Now' button
            shop_now_btn = self.wait.until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Shop Now"))
            )
            self.assertTrue(shop_now_btn.is_displayed(), "'Shop Now' button is not visible.")

            # Ensure no errors after interaction
            shop_now_btn.click()
            self.wait.until(EC.url_contains("localhost"))

        except Exception as e:
            self.fail(f"Test failed due to missing element or error: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()