import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_main_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check for header links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            tables_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            chairs_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))

            # Check links
            self.assertTrue(home_link.is_displayed(), "Home link is not visible")
            self.assertTrue(tables_link.is_displayed(), "Tables link is not visible")
            self.assertTrue(chairs_link.is_displayed(), "Chairs link is not visible")

            # Check for login elements
            login_tab = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@data-rb-event-key, 'login')]")))
            register_tab = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@data-rb-event-key, 'register')]")))

            self.assertTrue(login_tab.is_displayed(), "Login tab is not visible")
            self.assertTrue(register_tab.is_displayed(), "Register tab is not visible")

            # Interact with "Accept Cookies" button
            accept_cookies_btn = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies_btn.click()

            # Ensure no errors occurred after interaction
            self.assertTrue(accept_cookies_btn.is_displayed(), "Accept Cookies button interaction caused an error")

        except Exception as e:
            self.fail(f"Test case failed due to: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()