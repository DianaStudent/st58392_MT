from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShopUIElementsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check presence and visibility of important elements
        try:
            # Navigation Links
            home_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Home']")))
            tables_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Tables']")))
            chairs_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Chairs']")))
            
            # Login and Register Links
            driver.find_element(By.CSS_SELECTOR, '.account-setting-active').click()
            login_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Login']")))
            register_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Register']")))

            # Cookie Consent Button
            cookie_button = wait.until(EC.visibility_of_element_located((By.ID, 'rcc-confirm-button')))

            # Product Add to Cart Button
            add_to_cart_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Add to cart')]")))

        except Exception as e:
            self.fail(f"UI element not found or not visible: {str(e)}")

        # Interacting with elements
        try:
            # Accept cookies
            cookie_button.click()
            
            # Click on the first "Add to Cart" button
            add_to_cart_button.click()

            # Check that alert or any visual indication appears
            cart_status = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'No items added to cart')]")))
            self.assertIsNotNone(cart_status, "Cart status is not updated.")

        except Exception as e:
            self.fail(f"Failed during interaction or visual update: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()