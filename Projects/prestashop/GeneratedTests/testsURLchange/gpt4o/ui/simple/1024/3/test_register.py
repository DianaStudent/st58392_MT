import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class RegistrationPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/registration")  # Adjust URL as needed
        self.driver.maximize_window()

    def test_element_visibility(self):
        driver = self.driver

        try:
            # Check header
            header = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.TAG_NAME, "header"))
            )

            # Check page title
            page_title = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".page-header h1"))
            )
            self.assertIn("Create an account", page_title.text)

            # Check form fields
            form = driver.find_element(By.ID, "customer-form")
            WebDriverWait(driver, 20).until(
                EC.visibility_of_all_elements_located((By.TAG_NAME, "input"))
            )
            fname = form.find_element(By.ID, "field-firstname")
            lname = form.find_element(By.ID, "field-lastname")
            email = form.find_element(By.ID, "field-email")
            password = form.find_element(By.ID, "field-password")
            submit_button = form.find_element(By.CSS_SELECTOR, "button[type='submit']")

            for element in [form, fname, lname, email, password, submit_button]:
                self.assertTrue(element.is_displayed(), f"{element} is not visible")

        except Exception as e:
            self.fail(f"Test failed due to missing element: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()