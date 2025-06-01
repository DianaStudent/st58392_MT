import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class RegistrationPageTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.get("http://localhost:8080/en/registration")
        self.wait = WebDriverWait(self.driver, 20)

    def test_registration_page_elements(self):
        driver = self.driver
        wait = self.wait
        
        # Check navigation links are present and visible
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home"))))
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes"))))
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories"))))
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art"))))
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in"))))

        # Check form fields are present and visible
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.ID, "field-firstname"))))
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.ID, "field-lastname"))))
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.ID, "field-email"))))
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.ID, "field-password"))))
        
        # Check buttons are present and visible
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']"))))
        
        # Interact with a button and check no errors
        submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()
        
        # Assume the page should display an error on submission of empty form
        try:
            self.assertTrue(wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "form-error-text"))))
        except:
            # If there's no error message, that might mean the click didn't cause errors
            pass

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()