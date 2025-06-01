import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestMaxPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('http://max/')

    def test_main_ui_components_present(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'header')))
        
        header_title = (By.CSS_SELECTOR, '#header > .title')
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(header_title)).is_displayed())

        buttons = [ 
            (By.CSS_SELECTOR, '.button.button--primary'),
            (By.XPATH, '//button[@class="button button--primary"]') # Using both CSS and XPath selectors
        ]
        for button in buttons:
            self.assertTrue(WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(button)).is_displayed())

        links = [
            (By.LINK_TEXT, 'Login'),
            (By.XPATH, '//a[@href="login"]') # Using both link text and XPath selectors
        ]
        for link in links:
            self.assertTrue(WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(link)).is_displayed())

    def test_login_page_ui_components_present(self):
        login_link = (By.LINK_TEXT, 'Login')
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(login_link)).is_enabled())
        
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'login-form')))
        form_fields = [
            (By.NAME, 'username'),
            (By.NAME, 'password')
        ]
        for field in form_fields:
            self.assertTrue(WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(field)).is_displayed())

    def test_search_page_ui_components_present(self):
        search_link = (By.LINK_TEXT, 'Search')
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(search_link)).is_enabled())
        
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'search-form')))
        form_fields = [
            (By.NAME, 'q'),
            (By.NAME, 'submit')
        ]
        for field in form_fields:
            self.assertTrue(WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(field)).is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()