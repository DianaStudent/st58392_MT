import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestRegistrationPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/registration")

    def test_registration_page(self):
        # Check the presence and visibility of input fields, buttons, labels, and sections
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "firstName")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "lastName")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "emailAddress")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "password")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "reenterPassword")))

        # Check that the main UI components are present: headers, buttons, links, form fields, etc.
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='firstName']"))))
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-primary']"))))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()