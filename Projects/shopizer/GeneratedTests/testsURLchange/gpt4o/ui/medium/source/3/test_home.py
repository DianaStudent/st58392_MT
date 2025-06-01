import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_presence(self):
        driver = self.driver

        # Check navigation links
        try:
            home_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            tables_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            chairs_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
        except:
            self.fail("Navigation links are missing or not visible.")

        # Check buttons
        try:
            accept_cookies_button = self.wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
        except:
            self.fail("Accept cookies button is missing or not visible.")

        # Check presence of search and subscribe inputs
        try:
            subscribe_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='email']")))
        except:
            self.fail("Subscribe input is missing or not visible.")

        # Check banners
        try:
            banner_image = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".site-blocks-cover img")))
        except:
            self.fail("Banner image is missing or not visible.")

    def test_button_interaction(self):
        driver = self.driver

        # Interact with a button
        try:
            accept_cookies_button = self.wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
            self.wait.until(EC.invisibility_of_element(accept_cookies_button))
        except:
            self.fail("Failed to interact with the Accept cookies button.")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()