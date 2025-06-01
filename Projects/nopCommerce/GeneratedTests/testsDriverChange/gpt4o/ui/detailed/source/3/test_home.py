import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestHomePageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check header visibility
        try:
            header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header')))
        except:
            self.fail("Header is not visible")

        # Check footer visibility
        try:
            footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'footer')))
        except:
            self.fail("Footer is not visible")

        # Check register link visibility
        try:
            register_link = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'ico-register')))
        except:
            self.fail("Register link is not visible")

        # Check login link visibility
        try:
            login_link = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'ico-login')))
        except:
            self.fail("Login link is not visible")

        # Check search box visibility
        try:
            search_box = wait.until(EC.visibility_of_element_located((By.ID, 'small-search-box-form')))
        except:
            self.fail("Search box is not visible")

        # Interact with search form
        search_input = search_box.find_element(By.ID, 'small-searchterms')
        search_input.send_keys('test')
        search_button = search_box.find_element(By.CLASS_NAME, 'search-box-button')
        search_button.click()

        # Check if search results page is loaded
        try:
            wait.until(EC.url_contains('/search'))
        except:
            self.fail("Search results page did not load")

        # Check if notification bar is present and visible
        try:
            notification_bar = wait.until(EC.visibility_of_element_located((By.ID, 'bar-notification')))
        except:
            self.fail("Notification bar is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()