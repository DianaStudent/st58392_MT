import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestMainUI(unittest.TestCase):
    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('http://localhost/')

    def tearDown(self):
        self.driver.quit()

    def test_homepage_elements_present(self):
        try:
            # Wait for elements to be present and visible with a timeout of 20 seconds
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h1')))
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'button')))
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, 'Tables')))

            # Check if elements are visible
            self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, 'h1').is_displayed())
            self.assertTrue(self.driver.find_element(By.TAG_NAME, 'button').is_displayed())
            self.assertTrue(self.driver.find_element(By.LINK_TEXT, 'Tables').is_displayed())

        except:
            # If any required element is missing, fail the test
            self.fail('Required elements are not present or visible on the homepage')

    def test_tables_page_elements_present(self):
        try:
            # Navigate to tables page
            self.driver.get('http://localhost/category/tables')

            # Wait for elements to be present and visible with a timeout of 20 seconds
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h1')))
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'button')))
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, 'Chairs')))

            # Check if elements are visible
            self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, 'h1').is_displayed())
            self.assertTrue(self.driver.find_element(By.TAG_NAME, 'button').is_displayed())
            self.assertTrue(self.driver.find_element(By.LINK_TEXT, 'Chairs').is_displayed())

        except:
            # If any required element is missing, fail the test
            self.fail('Required elements are not present or visible on tables page')

    def test_chairs_page_elements_present(self):
        try:
            # Navigate to chairs page
            self.driver.get('http://localhost/category/chairs')

            # Wait for elements to be present and visible with a timeout of 20 seconds
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h1')))
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'button')))
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, 'Login')))

            # Check if elements are visible
            self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, 'h1').is_displayed())
            self.assertTrue(self.driver.find_element(By.TAG_NAME, 'button').is_displayed())
            self.assertTrue(self.driver.find_element(By.LINK_TEXT, 'Login').is_displayed())

        except:
            # If any required element is missing, fail the test
            self.fail('Required elements are not present or visible on chairs page')

    def test_login_page_elements_present(self):
        try:
            # Navigate to login page
            self.driver.get('http://localhost/login')

            # Wait for elements to be present and visible with a timeout of 20 seconds
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h1')))
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'button')))
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, 'username')))

            # Check if elements are visible
            self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, 'h1').is_displayed())
            self.assertTrue(self.driver.find_element(By.TAG_NAME, 'button').is_displayed())
            self.assertTrue(self.driver.find_element(By.NAME, 'username').is_displayed())

        except:
            # If any required element is missing, fail the test
            self.fail('Required elements are not present or visible on login page')

    def test_register_page_elements_present(self):
        try:
            # Navigate to register page
            self.driver.get('http://localhost/register')

            # Wait for elements to be present and visible with a timeout of 20 seconds
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h1')))
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'button')))
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, 'username')))

            # Check if elements are visible
            self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, 'h1').is_displayed())
            self.assertTrue(self.driver.find_element(By.TAG_NAME, 'button').is_displayed())
            self.assertTrue(self.driver.find_element(By.NAME, 'username').is_displayed())

        except:
            # If any required element is missing, fail the test
            self.fail('Required elements are not present or visible on register page')

if __name__ == '__main__':
    unittest.main()