from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestUIComponents(unittest.TestCase):

    def setUp(self):
        # Set up the webdriver with ChromeDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/registration")

    def test_ui_components(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Check if header is present
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except:
            self.fail("Header is not visible.")

        # Verify the main navigation elements
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/']")))
            clothes_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']")))
            accessories_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']")))
            art_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']")))
        except:
            self.fail("One or more navigation links are not visible.")

        # Verify links in the registration form
        try:
            login_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2Fregistration']")))
            register_form = wait.until(EC.visibility_of_element_located((By.ID, "customer-form")))
        except:
            self.fail("Login link or registration form is not visible.")

        # Verify form fields
        try:
            first_name_field = wait.until(EC.visibility_of_element_located((By.ID, "field-firstname")))
            last_name_field = wait.until(EC.visibility_of_element_located((By.ID, "field-lastname")))
            email_field = wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
            password_field = wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
        except:
            self.fail("One or more form fields are not visible.")
        
        # Verify options and checkboxes
        try:
            gender_mr_radio = wait.until(EC.visibility_of_element_located((By.ID, "field-id_gender-1")))
            gender_mrs_radio = wait.until(EC.visibility_of_element_located((By.ID, "field-id_gender-2")))
            terms_checkbox = wait.until(EC.visibility_of_element_located((By.NAME, "psgdpr")))
        except:
            self.fail("One or more options or checkboxes are not visible.")

    def tearDown(self):
        # Quit the WebDriver instance
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()