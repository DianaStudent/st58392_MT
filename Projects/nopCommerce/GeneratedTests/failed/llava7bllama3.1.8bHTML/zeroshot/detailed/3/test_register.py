from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestRegisterProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(html_data['homepage'])

    def test_register_process(self):
        # Open the homepage.
        self.assertEqual(self.driver.title, 'Homepage')

        # Click the "Register" link in the top navigation.
        register_link_selector = (By.XPATH, "//a[@href='{0}']".format(html_data['register_page']))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(register_link_selector))
        self.driver.find_element(*register_link_selector).click()

        # Wait for the registration form to load.
        register_form_selector = (By.XPATH, "//form[@id='register-form']")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(register_form_selector))

        # Select the appropriate gender radio input based on the provided data.
        gender_radio_selector = (By.ID, 'gender-female')
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(gender_radio_selector))
        self.driver.find_element(*gender_radio_selector).click()

        # Fill in all required fields: first name, last name, email, company name, password, confirm password from credentials.
        first_name_field_selector = (By.ID, 'first-name')
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(first_name_field_selector))
        self.driver.find_element(*first_name_field_selector).send_keys('Test')

        last_name_field_selector = (By.ID, 'last-name')
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(last_name_field_selector))
        self.driver.find_element(*last_name_field_selector).send_keys('User')

        email_field_selector = (By.ID, 'email')
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(email_field_selector))
        self.driver.find_element(*email_field_selector).send_keys(generate_email())

        company_name_field_selector = (By.ID, 'company-name')
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(company_name_field_selector))
        self.driver.find_element(*company_name_field_selector).send_keys('TestCorp')

        password_field_selector = (By.ID, 'password')
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(password_field_selector))
        self.driver.find_element(*password_field_selector).send_keys('test11')

        confirm_password_field_selector = (By.ID, 'confirm-password')
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(confirm_password_field_selector))
        self.driver.find_element(*confirm_password_field_selector).send_keys('test11')

        # Submit the registration form.
        register_button_selector = (By.ID, 'register-button')
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(register_button_selector))
        self.driver.find_element(*register_button_selector).click()

        # Wait for the response page or confirmation message to load.
        result_page_selector = (By.XPATH, "//div[@class='result']")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(result_page_selector))

        # Verify that registration succeeded by checking:
        # A confirmation text element is present - Its content includes "Your registration completed".
        self.assertTrue(self.driver.find_element(By.XPATH, "//div[@class='result']").text.strip().startswith('Your registration completed'))

def generate_email():
    import uuid
    return 'test{0}@test.com'.format(uuid.uuid4())

if __name__ == '__main__':
    unittest.main()