import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UIElementPresenceTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_ui_elements_visibility(self):
        driver = self.driver

        # Wait for and verify navigation links
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Home"))
            )
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Tables"))
            )
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Chairs"))
            )
        except:
            self.fail("Failed to find navigation links.")

        # Wait for and verify the 'Shop Now' button
        try:
            shop_now_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Shop Now"))
            )
        except:
            self.fail("Failed to find 'Shop Now' button.")

        # Test interaction: Click 'Shop Now' and check the banner exists after click
        try:
            shop_now_button.click()
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "site-block-cover-content"))
            )
        except:
            self.fail("Interacting with 'Shop Now' button caused an issue.")

        # Wait for and verify the 'Subscribe' form
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='email']"))
            )
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "button.button"))
            )
        except:
            self.fail("Failed to find 'Subscribe' form elements.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()