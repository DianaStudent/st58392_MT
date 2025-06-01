import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.assert_until import AssertUntil
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys

class TestRegisterPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_register_page(self):
        driver = self.driver
        base_url = "http://localhost:8080/en/"
        registration_url = base_url + "registration"

        # Test if the page loads successfully.
        driver.get(registration_url)
        self.wait.until(ExpectedConditions.visibilityOfElementLocated((By.XPATH, "//header[contains(text='Register')]")))
        self.wait.until(ExpectedConditions.visibilityOfElementLocated((By.XPATH, "//form[contains(id='register_form')]")))

        first_name_field = WebDriverWait(driver, 20).until(ExpectedConditions.visibilityOfElementLocated((By.XPATH, "//input[contains(@id,'first_name')]")))
        last_name_field = WebDriverWait(driver, 20).until(ExpectedConditions.visibilityOfElementLocated((By.XPATH, "//input[contains(@id,'last_name')]")))
        email_field = WebDriverWait(driver, 20).until(ExpectedConditions.visibilityOfElementLocated((By.XPATH, "//input[contains(@id,'email')]")))
        password_field = WebDriverWait(driver, 20).until(ExpectedConditions.visibilityOfElementLocated((By.XPATH, "//input[contains(@id,'password')]")))
        phone_number_field = WebDriverWait(driver, 20).until(ExpectedConditions.visibilityOfElementLocated((By.XPATH, "//input[contains(@id,'phone_number')]")))

        checkbox = WebDriverWait(driver, 20).until(ExpectedConditions.visibilityOfElementLocated((By.XPATH, "//div[contains(text,'I agree to the terms of service.')]")))
        self.wait.until(ExpectedConditions.visibilityOfElementLocated((By.XPATH, "//button[contains(@class,'btn btn-primary')][contains(@value,'Register')]")))

if __name__ == '__main__':
    unittest.main()