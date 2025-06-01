import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common Alert  import Alert
from selenium.webdriver.common Alert  import Alert

class TestEcommerceWebsite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_accessories_page(self):
        driver = self.driver
        url = "http://localhost:8080/6-accessories"
        driver.get(url)
        wait = self.wait

        # Check if main UI components are present and visible
        header = (By.XPATH, "//header")
        wait.until(lambda x: x.find_element(header))
        buttons = (By.XPATH, "//button")
        wait.until(lambda x: x.find_element(buttons))

        # Select the "Art" category
        select_category = Select(self.driver.find_element(by=By.XPATH, "//select"))
        select_category.select_by_visible_text("Art")

    def test_login_page(self):
        driver = self.driver
        url = "http://localhost:8080/login"
        driver.get(url)
        wait = self.wait

        # Locate the form fields and check if they exist and are visible
        username_field = (By.XPATH, "//input[@name='username']")
        password_field = (By.XPATH, "//input[@name='password']")
        wait.until(lambda x: x.find_element(username_field))
        wait.until(lambda x: x.find_element(password_field))

    def test_register_page(self):
        driver = self.driver
        url = "http://localhost:8080/registration"
        driver.get(url)
        wait = self.wait

        # Locate the form fields and check if they exist and are visible
        first_name_field = (By.XPATH, "//input[@name='first_name']")
        last_name_field = (By.XPATH, "//input[@name='last_name']")
        email_field = (By.XPATH, "//input[@name='email']")
        wait.until(lambda x: x.find_element(first_name_field))
        wait.until(lambda x: x.find_element(last_name_field))
        wait.until(lambda x: x.find_element(email_field))

if __name__ == '__main__':
    unittest.main()