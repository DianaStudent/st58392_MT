import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TestUIElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver

        # Verify navigation links
        try:
            home_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Home')))
            tables_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Tables')))
            chairs_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Chairs')))
            self.assertTrue(home_link.is_displayed())
            self.assertTrue(tables_link.is_displayed())
            self.assertTrue(chairs_link.is_displayed())
        except TimeoutException:
            self.fail("Navigation links are not visible")

        # Verify presence of buttons
        try:
            accept_cookies_button = self.wait.until(EC.visibility_of_element_located((By.ID, 'rcc-confirm-button')))
            self.assertTrue(accept_cookies_button.is_displayed())
        except TimeoutException:
            self.fail("Accept cookies button is not visible")

        # Click 'Accept' button and verify UI update
        accept_cookies_button.click()
        try:
            self.wait.until(EC.invisibility_of_element((By.CLASS_NAME, 'CookieConsent')))
        except TimeoutException:
            self.fail("Cookie consent did not disappear after clicking Accept")

        # Verify 'Add to cart' button presence
        try:
            add_to_cart_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Add to cart')]")))
            self.assertTrue(add_to_cart_button.is_displayed())
        except TimeoutException:
            self.fail("'Add to cart' button is not visible")

    # Interaction check - interact with 'Add to cart' button
        add_to_cart_button.click()
        try:
            cart_icon = self.wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'count-style'), '1'))
        except TimeoutException:
            self.fail("Cart was not updated after adding product")

if __name__ == "__main__":
    unittest.main()