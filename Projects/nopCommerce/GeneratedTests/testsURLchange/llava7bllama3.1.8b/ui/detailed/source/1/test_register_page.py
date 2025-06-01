import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestRegisterPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/register?returnUrl=%2F")

    def test_register_page_elements(self):
        # Ensure structural elements are visible
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))

        # Check presence and visibility of input fields, buttons, labels, and sections
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "firstname"))))
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "lastname"))))
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "email"))))
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "password"))))

        # Check 'Continue' or 'Next' button
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))))

    def test_interact_with_elements(self):
        # Interact with key UI elements (e.g., click buttons)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "continue"))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()