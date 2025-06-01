import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.headless = True  # run in headless mode
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    def test_login_page(self):
        self.driver.get("http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art")

        # Ensure structural elements are present
        header = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "header")))
        self.assertTrue(header.is_displayed())

        footer = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "footer")))
        self.assertTrue(footer.is_displayed())

        # Ensure input fields and buttons are present
        email_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "email")))
        password_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "password")))
        login_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))

        self.assertTrue(email_field.is_displayed())
        self.assertTrue(password_field.is_displayed())
        self.assertTrue(login_button.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()