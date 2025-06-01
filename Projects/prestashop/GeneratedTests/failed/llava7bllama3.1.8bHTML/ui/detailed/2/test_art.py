from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--headless')  # Remove '--headless' to run the test with browser visibility
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.get('http://localhost:8080/en/')

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):

        # Check main UI components
        header = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'header')))
        footer = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'footer')))

        navigation = self.driver.find_element(By.CSS_SELECTOR, '.nav')
        logo = self.driver.find_element(By.CSS_SELECTOR, '.logo')

        # Check input fields, buttons, labels and sections
        search_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'search_query_top')))
        submit_button = self.driver.find_element(By.NAME, 'submit_search')
        cart_button = self.driver.find_element(By.CSS_SELECTOR, '.cart-container')

        # Interact with key UI elements
        search_input.send_keys('Test product')
        submit_button.click()

        # Confirm that the UI reacts visually
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ul.products')))

        # Assert that no required UI element is missing
        self.failUnless(header.is_displayed())
        self.failUnless(footer.is_displayed())
        self.failUnless(navigation.is_displayed())
        self.failUnless(logo.is_displayed())
        self.failUnless(search_input.is_displayed())
        self.failUnless(submit_button.is_displayed())
        self.failUnless(cart_button.is_displayed())

    def test_login_page(self):
        # Go to login page
        self.driver.get('http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art')

        # Check login form elements
        username_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'email')))
        password_input = self.driver.find_element(By.ID, 'passwd')
        submit_button = self.driver.find_element(By.NAME, 'SubmitLogin')

        # Interact with key UI elements
        username_input.send_keys('test_user')
        password_input.send_keys('test_password')
        submit_button.click()

    def test_register_page(self):
        # Go to register page
        self.driver.get('http://localhost:8080/en/registration')

        # Check register form elements
        email_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'email')))
        password_input = self.driver.find_element(By.ID, 'passwd')
        submit_button = self.driver.find_element(By.NAME, 'SubmitCreate')

if __name__ == '__main__':
    unittest.main()