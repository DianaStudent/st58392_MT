from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class RegisterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get(html_data["home_before_register"])
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "__RequestVerificationToken")))

    def test_register_user(self):
        # Click on the register button
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//body/div[1]/div[2]/div[2]/form[1]/button")))
        self.driver.find_element(By.XPATH,
                                 "//body/div[1]/div[2]/div[2]/form[1]/button").click()

        # Wait for the registration page to load
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='page-title']/h1")))

        # Fill all fields
        self.driver.find_element(By.ID, "ConfirmPassword").send_keys("test11")
        self.driver.find_element(By.ID, "register-button").click()

        # Wait for the registration result page to load
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='result']")))

        # Verify that a message like 'Your registration completed' is shown after successful registration.
        message = self.driver.find_element(By.XPATH, "//div[@class='result']").text
        if message == "Your registration completed":
            print("Success")
        else:
            self.fail(f"Registration failed. Expected 'Your registration completed' but got {message}")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()