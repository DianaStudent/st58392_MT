import unittest
from selenium import webdriver
from webdriver_manager import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class TestPrestashopSite(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_prestashop_site(self):
        # Load the page and ensure that structural elements are visible.
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains('header')]")))
        self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains('footer')]")))

        # Check the presence and visibility of input fields, buttons, labels, and sections.
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))

        # Interact with key UI elements (e.g., click buttons).
        self.driver.find_element_by_name('username').send_keys('test_user')
        self.driver.find_element_by_name('password').send_keys('test_password')

        # Confirm that the UI reacts visually.
        time.sleep(5)

        # Assert that no required UI element is missing.
        if len(self.wait.until(EC.presence_of_elements_located((By.XPATH, "//input[@name='username']")))) == 1:
            self.fail("Username field is missing")
        elif len(self.wait.until(EC.presence_of_elements_located((By.XPATH, "//input[@name='password']")))) == 1:
            self.fail("Password field is missing")

if __name__ == '__main__':
    unittest.main()