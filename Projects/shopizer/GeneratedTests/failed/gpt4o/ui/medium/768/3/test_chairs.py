from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestWebPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header and navigation links
        try:
            header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-area")))
        except:
            self.fail("Header is not visible")

        try:
            home_link = driver.find_element(By.LINK_TEXT, "Home")
            tables_link = driver.find_element(By.LINK_TEXT, "Tables")
            chairs_link = driver.find_element(By.LINK_TEXT, "Chairs")
        except:
            self.fail("Navigation links are not present or visible")

        # Check button presence
        try:
            accept_cookies_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
        except:
            self.fail("Accept cookies button is not present or visible")

        # Check product section
        try:
            product_section = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shop-bottom-area")))
        except:
            self.fail("Product section is not visible")

        # Interact with an element and verify UI changes
        try:
            accept_cookies_button.click()
            # Verify button disappears (assumed behavior)
            wait.until(EC.invisibility_of_element(accept_cookies_button))
        except:
            self.fail("Failed to interact with accept cookies button or UI did not update")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()