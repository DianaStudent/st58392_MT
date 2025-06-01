import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestWebpage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def tearDown(self):
        self.driver.quit()

    def test_webpage_elements(self):
        # Navigate to the webpage
        self.driver.get('http://localhost/')

        # Wait and check for the presence of structural elements
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'header')))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'footer')))

        # Check for the presence and visibility of input fields, buttons, labels, and sections
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#loginForm input[type="text"]'))))
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#loginForm input[type="password"]'))))
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#loginForm button[type="submit"]'))))

        # Interact with key UI elements (e.g., click buttons)
        login_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Login"]')))
        login_button.click()

        # Confirm that the UI reacts visually
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.react-toast-notifications__container'))))

        # Assert that no required UI element is missing
        self.failUnlessElementPresent(By.XPATH, '//header', 'Header is not present')
        self.failUnlessElementPresent(By.XPATH, '//footer', 'Footer is not present')
        self.failUnlessElementPresent(By.CSS_SELECTOR, '#loginForm input[type="text"]', 'Input field for username is not present')
        self.failUnlessElementPresent(By.CSS_SELECTOR, '#loginForm input[type="password"]', 'Input field for password is not present')
        self.failUnlessElementPresent(By.CSS_SELECTOR, '#loginForm button[type="submit"]', 'Login button is not present')

    def failUnlessElementPresent(self, locator_type, locator_value, message):
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((locator_type, locator_value)))
        except TimeoutException as e:
            self.fail(message)

if __name__ == '__main__':
    unittest.main()