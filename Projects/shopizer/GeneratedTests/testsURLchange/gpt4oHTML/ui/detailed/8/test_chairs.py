import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver: WebDriver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # 1. Ensure main structural elements are visible
        try:
            header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area")))
            footer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer.footer-area")))
            self.assertTrue(header.is_displayed(), "Header is not visible")
            self.assertTrue(footer.is_displayed(), "Footer is not visible")
        except Exception as e:
            self.fail(f"Failed in header/footer check: {e}")

        # 2. Check presence and visibility of main UI components
        try:
            navigation_links = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "nav ul li a")))
            self.assertGreater(len(navigation_links), 0, "Navigation links are missing or not visible")
            for link in navigation_links:
                self.assertTrue(link.is_displayed(), f"Navigation link {link.text} is not visible")

            cookie_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            self.assertTrue(cookie_button.is_displayed(), "Accept cookies button is not visible")

            # Ensure buttons, input fields from header are visible
            account_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".account-setting-active")))
            cart_icon = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".icon-cart")))

            self.assertTrue(account_button.is_displayed(), "Account button is not visible")
            self.assertTrue(cart_icon.is_displayed(), "Cart icon is not visible")

        except Exception as e:
            self.fail(f"Failed in UI components check: {e}")

        # 3. Interact with key UI elements
        try:
            cookie_button.click()
            wait.until(EC.invisibility_of_element(cookie_button))

            home_link = driver.find_element(By.CSS_SELECTOR, "nav ul li a[href='/']")
            home_link.click()
            wait.until(EC.url_to_be("http://localhost/"))

        except Exception as e:
            self.fail(f"Failure during interaction with UI elements: {e}")

        # 4. Assert no required UI element is missing
        try:
            shop_area = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".shop-area")))
            self.assertTrue(shop_area.is_displayed(), "Shop area is not visible")
        except Exception as e:
            self.fail(f"Required UI element check failed: {e}")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()