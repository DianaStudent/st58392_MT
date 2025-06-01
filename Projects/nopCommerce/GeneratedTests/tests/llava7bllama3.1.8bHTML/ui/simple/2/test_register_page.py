import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TestMaxWebsite(unittest.TestCase):
    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")

    def tearDown(self):
        self.driver.quit()

    def test_main_ui_components(self):
        # Check that the main UI components are present: headers, buttons, links, form fields, etc.
        wait = WebDriverWait(self.driver, 20)
        
        # Check header
        header = wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        self.assertIsNotNone(header.text)

        # Check button(s) and links
        buttons_and_links = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button | //a")))
        for element in buttons_and_links:
            self.assertIsNotNone(element.get_attribute("href"))

        # Check form fields
        form_fields = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "input")))
        for field in form_fields:
            self.assertIsNotNone(field.get_attribute("type"))
            if field.get_attribute("type") == "email":
                continue
            elif field.get_attribute("type") == "password":
                continue
            else:
                self.assertIsNotNone(field.get_attribute("placeholder"))

    def test_login_page(self):
        # Check that the login page elements are present: form fields, buttons, links
        wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://max/login?returnUrl=%2F")
        
        # Check form fields
        form_fields = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "input")))
        for field in form_fields:
            if field.get_attribute("type") == "email":
                continue
            elif field.get_attribute("type") == "password":
                continue
            else:
                self.assertIsNotNone(field.get_attribute("placeholder"))

    def test_register_page(self):
        # Check that the register page elements are present: form fields, buttons, links
        wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://max/register?returnUrl=%2F")
        
        # Check form fields
        form_fields = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "input")))
        for field in form_fields:
            if field.get_attribute("type") == "email":
                continue
            elif field.get_attribute("type") == "password":
                continue
            else:
                self.assertIsNotNone(field.get_attribute("placeholder"))

    def test_search_page(self):
        # Check that the search page elements are present: form fields, buttons, links
        wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://max/search")
        
        # Check form fields
        form_fields = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "input")))
        for field in form_fields:
            if field.get_attribute("type") == "email":
                continue
            elif field.get_attribute("type") == "password":
                continue
            else:
                self.assertIsNotNone(field.get_attribute("placeholder"))

if __name__ == "__main__":
    unittest.main()