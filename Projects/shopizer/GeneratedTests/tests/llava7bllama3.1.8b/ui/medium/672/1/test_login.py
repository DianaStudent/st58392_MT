import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost/login")

    def test_ui_components(self):
        # Confirm the presence of key interface elements
        self.assertGreater(len(self.driver.find_elements(By.TAG_NAME, 'nav')), 0)
        self.assertGreater(len(self.driver.find_elements(By.TAG_NAME, 'input')), 0)
        self.assertGreater(len(self.driver.find_elements(By.TAG_NAME, 'button')), 0)

        # Confirm the presence of specific elements
        login_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        register_link = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/register']")))

        # Interact with one element and verify the UI updates visually
        login_button.click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".react-toast-notifications__container")))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()