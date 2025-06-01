import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('http://localhost/')

    def test_structure_elements_visible(self):
        # Header
        header_title = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1")))
        self.assertEqual(header_title.text, 'Home', msg='Header title is not correct')
        
        # Footer
        footer_text = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//footer/p")))
        self.assertIn('Copyright', footer_text.text, msg='Footer text is missing copyright')

    def test_page_elements_visible(self):
        # Navigation links
        nav_links = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'ul li a')))
        for link in nav_links:
            self.assertTrue(link.is_displayed(), msg='Navigation link is not visible')
        
        # Form fields
        form_input_fields = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//input[@type='text']")))
        for field in form_input_fields:
            self.assertTrue(field.is_enabled() and field.is_displayed(), msg='Form input is not visible')

    def test_ui_interactions(self):
        # Click on login button
        login_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[text()='Login']")))
        login_button.click()

        # Check if we are redirected to the login page
        self.assertEqual(self.driver.current_url, 'http://localhost/login')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()