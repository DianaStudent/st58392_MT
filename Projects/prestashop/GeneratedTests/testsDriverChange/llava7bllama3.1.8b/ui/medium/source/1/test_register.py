import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class TestRegisterPage(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        self.driver.get("http://localhost:8080/en/registration")

    def test_register_page(self):
        # Verify presence of key interface elements
        navigation_links = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.navbar-nav li")))
        inputs = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[name]")))
        buttons = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button[type]")))
        banners = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".banner")))

        # Interact with one or two elements
        register_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        register_button.click()

        # Verify that interactive elements do not cause errors in the UI
        self.assertTrue(register_button.is_enabled())
        self.assertEqual(self.driver.title, "Registration")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()