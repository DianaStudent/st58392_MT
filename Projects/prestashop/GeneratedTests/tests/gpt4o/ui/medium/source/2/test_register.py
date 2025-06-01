import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/registration")

    def test_elements_visibility(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check navigation links
        nav_links = {
            "home": "http://localhost:8080/en/",
            "clothes": "http://localhost:8080/en/3-clothes",
            "accessories": "http://localhost:8080/en/6-accessories",
            "art": "http://localhost:8080/en/9-art"
        }

        for link_text, url in nav_links.items():
            try:
                element = wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, link_text)))
                self.assertEqual(element.get_attribute("href"), url)
            except Exception as e:
                self.fail(f"Navigation link '{link_text}' not found or not visible: {str(e)}")

        # Check input fields
        input_ids = ["field-firstname", "field-lastname", "field-email", "field-password", "field-birthday"]

        for input_id in input_ids:
            try:
                element = wait.until(EC.visibility_of_element_located((By.ID, input_id)))
            except Exception as e:
                self.fail(f"Input field '{input_id}' not found or not visible: {str(e)}")

        # Check button
        try:
            submit_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".form-control-submit")))
        except Exception as e:
            self.fail(f"Submit button not found or not visible: {str(e)}")

        # Interaction Check: Click submit button
        try:
            submit_button.click()
            # For simplicity, expect the page to attempt a reload on submit
            wait.until(EC.url_changes("http://localhost:8080/en/registration"))
        except Exception as e:
            self.fail(f"Error clicking submit button or updating page: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()