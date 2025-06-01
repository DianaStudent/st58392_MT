import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alerts import Alert

class TestLoginScenario(unittest.TestCase):
    @classmethod
    def setUp(self):
        options = Options()
        options.headless = False
        driver_path = "C:\chromedriver.exe"
        self.driver = webdriver.Chrome(driver_path, options=options)

    def test_login_scenario(self):
        self.driver.get("http://localhost:8080/en/")
        login_link = WebDriverWait(self.driver, 20).until(
            EC.element_located((By.XPATH, "//div[contains(text(), 'login')]"))
        )
        login_link.click()
        email_field = WebDriverWait(self.driver, 20).until(
            EC.element_located((By.XPATH, "//input[@name='email']"))
        )
        email_field.send_keys("test@user.com")
        password_field = WebDriverWait(self.driver, 20).until(
            EC.element_located((By.XPATH, "//input[@name='password']"))
        )
        password_field.send_keys("test@user1")
        submit_button = WebDriverWait(self.driver, 20).until(
            EC.element_located((By.XPATH, "//button[contains(text(), 'submit')]"))
        )
        submit_button.click()
        WebDriverWait(self.driver, 20).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Sign out')]"))
        )
        username_text = self.driver.find_element_by_xpath("//span[contains(text(), 'test user')]")

        if username_text is not None and username_text.get_attribute("data-name") == "test user":
            print("Login was successful")
            self.assertTrue(username_text.is_displayed())
        else:
            print("Login failed")
            self.fail()

    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()