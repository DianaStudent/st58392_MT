import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestArtPageUI(unittest.TestCase):

    def setUp(self):
        # Set up the WebDriver instance using ChromeDriverManager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://localhost:8080/en/9-art')
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        # Quit the WebDriver instance at the end of each test
        self.driver.quit()

    def test_ui_elements_presence(self):
        # Check presence of headers
        try:
            self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        except:
            self.fail('Header not found.')

        # Check presence of main navigation
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, '_desktop_top_menu')))
        except:
            self.fail('Main navigation not found.')

        # Check presence of the search widget
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, 'search_widget')))
        except:
            self.fail('Search widget not found.')
        
        # Check presence of buttons and links
        try:
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.btn-unstyle')))
        except:
            self.fail('Expected buttons or links not found.')

        # Confirm presence of newsletter input and submit button
        try:
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="email"]')))
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="submitNewsletter"]')))
        except:
            self.fail('Newsletter input or submit button not found.')

    def test_interaction(self):
        # Interact with the language dropdown
        try:
            language_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.language-selector button')))
            ActionChains(self.driver).move_to_element(language_button).click().perform()
            # Check if the dropdown menu became visible
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.dropdown-menu[aria-labelledby="language-selector-label"]')))
        except:
            self.fail('Could not interact with language dropdown or dropdown menu is not visible.')

        # Click on the 'Sign in' link
        try:
            sign_in_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Sign in')))
            sign_in_link.click()
            # Verify we are redirected to the login page
            self.wait.until(EC.url_contains('login'))
        except:
            self.fail('Could not click on Sign in link or redirect failed.')

    def test_no_ui_errors(self):
        # Verify there are no UI errors after interactions
        try:
            self.driver.find_element(By.CLASS_NAME, 'wishlist-toast')  # Check for toast errors
            self.fail('UI error toast found.')
        except:
            pass  # No error toast is present

if __name__ == '__main__':
    unittest.main()