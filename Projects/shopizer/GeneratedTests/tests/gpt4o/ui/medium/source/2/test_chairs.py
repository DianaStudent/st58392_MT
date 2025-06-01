import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class KeyUIElementsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Verify Header Elements
        try:
            header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-area")))
            self.assertTrue(header.is_displayed(), "Header is not visible")

            # Check navigation links
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            self.assertTrue(home_link.is_displayed(), "Home link is not visible")

            tables_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            self.assertTrue(tables_link.is_displayed(), "Tables link is not visible")

            chairs_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
            self.assertTrue(chairs_link.is_displayed(), "Chairs link is not visible")
        except Exception as e:
            self.fail(f"Navigation link check failed: {str(e)}")

        # Verify Buttons and Interactions
        try:
            accept_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            self.assertTrue(accept_cookies_button.is_displayed(), "Accept cookies button is not visible")
            accept_cookies_button.click()
        except Exception as e:
            self.fail(f"Accept cookies button interaction failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()