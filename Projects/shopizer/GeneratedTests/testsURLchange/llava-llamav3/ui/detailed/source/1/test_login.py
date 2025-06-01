import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.assertions import Assert

class TestShopsterLoginPage(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(ChromeDriverManager().get_chrome_driver())
        self.driver = driver

    def tearDown(self):
        self.driver.quit()

    def test_load_page(self):
        self.driver.get("http://localhost/")
        assert "Shopster" in self.driver.title, "Title not match"
        self.assertTrue(self.driver.find_element_by_tag_name("header"))
        self.assertTrue(self.driver.find_element_by_tag_name("footer"))

    def test_check_required_elements(self):
        self.driver.get("http://localhost/login")
        for required_field in ["Name", "Email", "Password"]:
            assert self.driver.find_element_by_name(required_field), f"{required_field} field not found"
        self.assertTrue(self.driver.find_element_by_name("Remember me"))
        self.assertTrue(self.driver.find_element_by_name("Login"))

    def test_interact_with_ui_elements(self):
        self.driver.get("http://localhost/login")
        email = self.driver.find_element_by_name("Email")
        password = self.driver.find_element_by_name("Password")
        remember_me = self.driver.find_element_by_name("Remember me")
        login_button = self.driver.find_element_by_name("Login")

        email.send_keys("test@example.com")
        password.send_keys("password")
        remember_me.click()
        login_button.click()

    def test_confirm_ui_reaction(self):
        self.driver.get("http://localhost/login")
        for required_field in ["Name", "Email", "Password"]:
            assert self.driver.find_element_by_name(required_field), f"{required_field} field not found"
        self.assertTrue(self.driver.find_element_by_name("Remember me"))
        self.assertTrue(self.driver.find_element_by_name("Login"))

    def test_required_elements(self):
        self.driver.get("http://localhost/login")
        for required_field in ["Name", "Email", "Password"]:
            assert self.driver.find_element_by_name(required_field), f"{required_field} field not found"
        self.assertTrue(self.driver.find_element_by_name("Remember me"))
        self.assertTrue(self.driver.find_element_by_name("Login"))

if __name__ == "__main__":
    unittest.main()