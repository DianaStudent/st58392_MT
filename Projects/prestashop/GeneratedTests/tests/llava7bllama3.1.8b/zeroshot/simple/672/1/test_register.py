from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager

class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")

    def test_register_simple(self):
        # Enter email address and password
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@data-name='Email']"))).send_keys("test@user1")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@data-name='Password']"))).send_keys("test@user1")

        # Fill all fields for registration and check checkboxes
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//input[@type='checkbox']")))

        # Find 'Register' button and click it
        register_button = self.driver.find_element(By.XPATH, "//button[@data-name='Register']")
        register_button.click()

        # Confirm success by checking that the text "Sign out" appear
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[text()='Sign out']")))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()