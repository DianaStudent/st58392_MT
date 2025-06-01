from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebsiteUITest(unittest.TestCase):

    def setUp(self):
        # Initialize the Chrome driver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost/")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Validate presence and visibility of header links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Home']")))
            tables_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Tables']")))
            chairs_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Chairs']")))
        except:
            self.fail("One or more navigation links are missing.")

        # Validate presence and visibility of account section
        try:
            account_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".account-setting-active")))
        except:
            self.fail("Account button is missing.")

        # Validate and interact with the 'Accept' cookies button
        try:
            accept_cookies_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
        except:
            self.fail("Cookies accept button is missing or not clickable.")

        # Validate presence and visibility of footer
        try:
            footer_text = wait.until(EC.visibility_of_element_located((By.XPATH, "//footer[@class='footer-area bg-gray pt-100 pb-70']")))
        except:
            self.fail("Footer is missing.")

    def tearDown(self):
        # Quit the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()