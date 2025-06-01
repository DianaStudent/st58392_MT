from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import uuid

class TestRegisterPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")

    def tearDown(self):
        self.driver.quit()

    def test_register_page(self):
        # Generate a random email
        self.email = f"test{uuid.uuid4()}@example.com"
        
        # Click on register button
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='__RequestVerificationToken']"))).click()
        
        # Fill all fields for registration
        self.driver.find_element(By.ID, "FirstName").send_keys("Test")
        self.driver.find_element(By.ID, "LastName").send_keys("User")
        self.driver.find_element(By.ID, "Email").send_keys(self.email)
        self.driver.find_element(By.ID, "Company").send_keys("Test Company")
        self.driver.find_element(By.NAME, "Gender").click()
        
        # Fill password and confirm password
        self.driver.find_element(By.ID, "Password").send_keys("test11")
        self.driver.find_element(By.ID, "ConfirmPassword").send_keys("test11")
        
        # Click on register button
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='register-next-step-button']"))).click()
        
        # Check if success message is shown after successful registration
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='result' and text()='Your registration completed']")))
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='result' and text()='Your registration completed']"))))

if __name__ == "__main__":
    unittest.main()