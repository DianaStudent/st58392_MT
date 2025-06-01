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
        self.driver.get("http://localhost/login")
    
    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Check navigation links
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))

            # Check presence of login elements
            wait.until(EC.visibility_of_element_located((By.NAME, "username")))
            wait.until(EC.visibility_of_element_located((By.NAME, "loginPassword")))

            # Check presence of buttons
            login_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button/span[text()='Login']")))
            register_tab = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@data-rb-event-key='register']")))

            # Interact with elements
            register_tab.click()
            wait.until(EC.visibility_of_element_located((By.NAME, "email")))

            login_button.click()

            # Check footer elements
            wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[text()='Address']")))
            wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[text()='USEFUL LINKS']")))
            wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[text()='Subscribe']")))

        except Exception as e:
            self.fail(f"Test failed due to missing element: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()