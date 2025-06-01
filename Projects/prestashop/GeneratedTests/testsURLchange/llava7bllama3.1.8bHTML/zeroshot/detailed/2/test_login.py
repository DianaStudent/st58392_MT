import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/en/")  # URL of your application

    def test_login(self):
        login_link = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Login"))
        )
        login_link.click()

        email_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )

        password_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )

        email_input.send_keys("test@user.com")
        password_input.send_keys("test@user1")

        submit_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "submit"))
        )
        submit_button.click()

        # Wait for redirect
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Sign out"))
        )

        sign_out_link = self.driver.find_element_by_link_text("Sign out")
        username = self.driver.find_element_by_xpath("//div[@data-name='username']").text

        assert "Sign out" in sign_out_link.text
        assert username != ""

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()