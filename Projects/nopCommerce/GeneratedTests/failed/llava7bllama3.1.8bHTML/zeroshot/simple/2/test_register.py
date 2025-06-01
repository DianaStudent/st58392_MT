from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

class TestRegisterProcess(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_register_process(self):
        self.driver.get("http://max/")  # replace with your url

        email = "test_email" + str(self.random_number()) + "@example.com"
        password = "test11"

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='__RequestVerificationToken']")))

        self.driver.find_element(By.NAME, "__RequestVerificationToken").send_keys("any_token")  # replace with your token

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='page registration-page']//form"))).click()

        first_name = "Test"
        last_name = "User"
        gender_male = self.driver.find_element(By.ID, "gender-male")
        gender_female = self.driver.find_element(By.ID, "gender-female")

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "__RequestVerificationToken")))

        if gender_male.is_enabled():
            gender_male.click()
        elif gender_female.is_enabled():
            gender_female.click()

        email_input = self.driver.find_element(By.ID, "Email")
        password_input = self.driver.find_element(By.ID, "Password")
        confirm_password_input = self.driver.find_element(By.ID, "ConfirmPassword")

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "__RequestVerificationToken")))

        email_input.send_keys(email)
        password_input.send_keys(password)
        confirm_password_input.send_keys(password)

        register_button = self.driver.find_element(By.ID, "register-button")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "register-button")))

        register_button.click()

        result_message = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='result']")))
        self.assertEqual(result_message.text.strip(), "Your registration completed")

    def random_number(self):
        import random
        return random.randint(1, 1000)

if __name__ == "__main__":
    unittest.main()