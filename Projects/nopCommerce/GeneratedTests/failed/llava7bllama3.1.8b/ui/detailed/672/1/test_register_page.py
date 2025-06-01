from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/register?returnUrl=%2F")

    def test_structural_elements(self):
        # Check that header, footer and navigation are visible
        self.assertTrue(self.driver.find_element(By.TAG_NAME, "header").is_displayed())
        self.assertTrue(self.driver.find_element(By.TAG_NAME, "footer").is_displayed())
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Home")))

    def test_input_fields_buttons_labels_sections(self):
        # Check that input fields, buttons and labels are present
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "firstName")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "lastName")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "emailAddress")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "password")))
        
        # Check that buttons are clickable
        self.assertTrue(self.driver.find_element(By.ID, "register").is_enabled())
        self.assertTrue(self.driver.find_element(By.LINK_TEXT, "Back to Login").is_enabled())

    def test_interaction_with_key_ui_elements(self):
        # Click on the register button and confirm it's visually reacting
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "register"))).click()
        self.assertTrue(self.driver.find_element(By.ID, "register").is_enabled())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()