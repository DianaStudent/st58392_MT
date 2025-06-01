import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginSimple(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # Use your preferred browser here

    def test_login_simple(self):
        self.driver.get("http://max/")

        # Confirm the page is loaded correctly
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='master-wrapper-page']")))

        # Login form
        login_form = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "main")))
        email_input = login_form.find_element(By.NAME, "Email")
        password_input = login_form.find_element(By.XPATH, "//label[@for='Password']/following-sibling::input")

        # Enter credentials
        email_input.send_keys("admin@admin.com")
        password_input.send_keys("admin")

        # Login button
        login_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='button-1 login-button']")))
        login_button.click()

        # Check if the "Log out" button is present in the top navigation after successful login.
        logout_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()