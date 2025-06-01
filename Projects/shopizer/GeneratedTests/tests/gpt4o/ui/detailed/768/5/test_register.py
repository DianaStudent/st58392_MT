import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header elements
        header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.logo img')))
        nav_home = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Home')))
        nav_tables = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Tables')))
        nav_chairs = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Chairs')))
        
        # Check footer elements
        footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        subscribe_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.button')))

        # Navigate to login/register page
        register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Register')))
        register_link.click()
        
        # Check form elements
        input_email = wait.until(EC.visibility_of_element_located((By.NAME, 'email')))
        input_password = wait.until(EC.visibility_of_element_located((By.NAME, 'password')))
        input_repeat_password = wait.until(EC.visibility_of_element_located((By.NAME, 'repeatPassword')))
        input_first_name = wait.until(EC.visibility_of_element_located((By.NAME, 'firstName')))
        input_last_name = wait.until(EC.visibility_of_element_located((By.NAME, 'lastName')))
        select_country = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'select')))
        input_state = wait.until(EC.visibility_of_element_located((By.NAME, 'stateProvince')))
        register_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.button-box button')))

        # Ensure all critical UI elements are present
        self.assertTrue(header.is_displayed())
        self.assertTrue(logo.is_displayed())
        self.assertTrue(nav_home.is_displayed())
        self.assertTrue(nav_tables.is_displayed())
        self.assertTrue(nav_chairs.is_displayed())
        self.assertTrue(footer.is_displayed())
        self.assertTrue(subscribe_button.is_displayed())
        self.assertTrue(input_email.is_displayed())
        self.assertTrue(input_password.is_displayed())
        self.assertTrue(input_repeat_password.is_displayed())
        self.assertTrue(input_first_name.is_displayed())
        self.assertTrue(input_last_name.is_displayed())
        self.assertTrue(select_country.is_displayed())
        self.assertTrue(input_state.is_displayed())
        self.assertTrue(register_button.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()