import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIComponents(unittest.TestCase):

    def setUp(self):
        # Set up the Chrome WebDriver
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Run in headless mode for testing
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.get('http://max/search')

    def test_main_ui_components_exist(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check if the header is present
        try:
            header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header')))
        except:
            self.fail('Header is missing.')

        # Check if the search box is present
        try:
            search_box = wait.until(EC.visibility_of_element_located((By.ID, 'small-searchterms')))
        except:
            self.fail('Search box is missing.')

        # Check if the search button is present
        try:
            search_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-button')))
        except:
            self.fail('Search button is missing.')

        # Check if the register link is present
        try:
            register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Register')))
        except:
            self.fail('Register link is missing.')

        # Check if the login link is present
        try:
            login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Log in')))
        except:
            self.fail('Log in link is missing.')

        # Check if cart link is present
        try:
            cart_link = wait.until(EC.visibility_of_element_located((By.ID, 'topcartlink')))
        except:
            self.fail('Shopping cart link is missing.')

    def tearDown(self):
        # Quit the driver
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()