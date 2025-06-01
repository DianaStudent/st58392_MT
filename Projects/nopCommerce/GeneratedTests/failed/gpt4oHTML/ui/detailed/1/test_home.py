from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check header existence and visibility
        try:
            header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header')))
        except:
            self.fail("Header is not present or visible")

        # Check footer existence and visibility
        try:
            footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'footer')))
        except:
            self.fail("Footer is not present or visible")

        # Check navigation links
        try:
            nav_links = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'top-menu')))
        except:
            self.fail("Navigation links are not present or visible")

        # Check presence and visibility of input fields
        try:
            search_box = wait.until(EC.visibility_of_element_located((By.ID, 'small-searchterms')))
        except:
            self.fail("Search box is not present or visible")

        # Check presence and visibility of buttons
        try:
            search_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.button-1.search-box-button')))
        except:
            self.fail("Search button is not present or visible")

        try:
            register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Register')))
        except:
            self.fail("Register link is not present or visible")

        try:
            login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Log in')))
        except:
            self.fail("Login link is not present or visible")

        # Interact with UI elements
        search_box.send_keys("Test")
        search_button.click()
        
        # Confirm UI reacts visually
        try:
            wait.until(EC.visibility_of_element_located((By.ID, 'ui-id-1')))
        except:
            self.fail("UI did not react as expected to search")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()