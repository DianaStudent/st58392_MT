import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/registration")

    def test_ui_components(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check for presence of navigation links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/']")))
            clothes_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']")))
            accessories_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']")))
            art_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']")))

            # Check form fields presence
            firstname_input = wait.until(EC.visibility_of_element_located((By.ID, "field-firstname")))
            lastname_input = wait.until(EC.visibility_of_element_located((By.ID, "field-lastname")))
            email_input = wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
            password_input = wait.until(EC.visibility_of_element_located((By.ID, "field-password")))

            # Check buttons presence
            signup_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit' and @data-link-action='save-customer']")))

            # Check interaction doesn't cause errors
            signup_button.click()
            error_elements = driver.find_elements(By.CLASS_NAME, 'form-control-comment')
            self.assertTrue(all(ele.text == "" for ele in error_elements), "Errors found in form inputs.")

        except Exception as e:
            self.fail(f"UI component test failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()