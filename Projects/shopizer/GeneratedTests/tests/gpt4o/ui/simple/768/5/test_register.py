import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/login")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver

        # Check header elements
        try:
            header_logo = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='logo']/a/img"))
            )
            self.assertTrue(header_logo.is_displayed(), "Header logo is not visible")

            home_link = self.wait.until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Home"))
            )
            self.assertTrue(home_link.is_displayed(), "Home link is not visible")

            tables_link = self.wait.until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Tables"))
            )
            self.assertTrue(tables_link.is_displayed(), "Tables link is not visible")

            chairs_link = self.wait.until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Chairs"))
            )
            self.assertTrue(chairs_link.is_displayed(), "Chairs link is not visible")

        except:
            self.fail("Header elements are missing or not visible")

        # Check form elements on login/register page
        try:
            login_tab = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//a[@data-rb-event-key='login']/h4"))
            )
            self.assertTrue(login_tab.is_displayed(), "Login tab is not visible")

            register_form = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//form"))
            )
            self.assertTrue(register_form.is_displayed(), "Register form is not visible")

            email_input = self.wait.until(
                EC.visibility_of_element_located((By.NAME, "email"))
            )
            self.assertTrue(email_input.is_displayed(), "Email input is not visible")

            password_input = self.wait.until(
                EC.visibility_of_element_located((By.NAME, "password"))
            )
            self.assertTrue(password_input.is_displayed(), "Password input is not visible")

            repeat_password_input = self.wait.until(
                EC.visibility_of_element_located((By.NAME, "repeatPassword"))
            )
            self.assertTrue(repeat_password_input.is_displayed(), "Repeat Password input is not visible")

            register_button = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//button/span[text()='Register']"))
            )
            self.assertTrue(register_button.is_displayed(), "Register button is not visible")

        except:
            self.fail("Form elements are missing or not visible")

        # Check footer elements
        try:
            copyright_text = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='copyright']/p"))
            )
            self.assertTrue(copyright_text.is_displayed(), "Copyright text is not visible")

            contact_email = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//a[contains(@href, 'mailto')]"))
            )
            self.assertTrue(contact_email.is_displayed(), "Contact email is not visible")

        except:
            self.fail("Footer elements are missing or not visible")


if __name__ == '__main__':
    unittest.main()