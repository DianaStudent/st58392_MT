import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestShopizerUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_UI_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Verify navigation links
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            tables_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            chairs_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
            self.assertTrue(home_link.is_displayed(), "Home link not visible")
            self.assertTrue(tables_link.is_displayed(), "Tables link not visible")
            self.assertTrue(chairs_link.is_displayed(), "Chairs link not visible")

            # Verify header logo
            logo_img = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".logo img")))
            self.assertTrue(logo_img.is_displayed(), "Logo image not visible")

            # Verify login and register links
            login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
            register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
            self.assertTrue(login_link.is_displayed(), "Login link not visible")
            self.assertTrue(register_link.is_displayed(), "Register link not visible")

            # Verify accept cookies button
            accept_cookies_btn = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            self.assertTrue(accept_cookies_btn.is_displayed(), "Accept cookies button not visible")

            # Click accept cookies button and verify no error occurs
            accept_cookies_btn.click()

            # Verify cart button
            cart_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".icon-cart")))
            self.assertTrue(cart_btn.is_displayed(), "Cart button not visible")

            # Interact with cart button to ensure no errors
            cart_btn.click()
            empty_cart_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart-content p")))
            self.assertTrue("No items added to cart" in empty_cart_message.text, "Expected empty cart message not present")

        except Exception as e:
            self.fail(f"Test failed due to an exception: {str(e)}")

if __name__ == "__main__":
    unittest.main()