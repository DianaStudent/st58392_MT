from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestLoginProcess(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_login_process(self):
        # Click the account icon and open the login form
        account_icon = WebDriverWait(self.driver, 20).until(EC.element_located((By.XPATH, "//a[@data-target='#loginModal']"))))
        ActionChains(self.driver).move_to_element(account_icon).click().perform()

        # Confirm success by checking the URL
        login_url = self.driver.current_url
        if "/my-account" not in login_url:
            self.fail("Failed to redirect to the account page")

if __name__ == '__main__':
    unittest.main()