import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class RegistrationPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/registration")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Checking presence of key elements: form elements
            social_title = wait.until(EC.visibility_of_element_located((By.ID, 'field-id_gender-1')))
            first_name = driver.find_element(By.ID, 'field-firstname')
            last_name = driver.find_element(By.ID, 'field-lastname')
            email = driver.find_element(By.ID, 'field-email')
            password = driver.find_element(By.ID, 'field-password')
            submit_button = driver.find_element(By.CSS_SELECTOR, 'button.btn-primary.form-control-submit')

            # Check if the header is present
            header = driver.find_element(By.TAG_NAME, 'h1')
            self.assertIn("Create an account", header.text)

            # Check if we can interact with the "Mr." radio button
            social_title.click()
            self.assertTrue(social_title.is_selected(), "Failed to select 'Mr.' radio button")

            # Check for the presence of other essential components
            home_link = driver.find_element(By.LINK_TEXT, 'Home')
            clothes_link = driver.find_element(By.LINK_TEXT, 'Clothes')
            accessories_link = driver.find_element(By.LINK_TEXT, 'Accessories')
            art_link = driver.find_element(By.LINK_TEXT, 'Art')
            login_link = driver.find_element(By.LINK_TEXT, 'Sign in')

            # Verify all elements exist and are visible
            elements = [first_name, last_name, email, password, submit_button,
                        home_link, clothes_link, accessories_link, art_link, login_link]

            for element in elements:
                self.assertTrue(element.is_displayed(), f"Element {element} is not visible.")

        except (TimeoutException, NoSuchElementException) as e:
            self.fail(f"Test failed due to a missing element or timeout: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()