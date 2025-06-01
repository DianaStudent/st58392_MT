import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/login")
        self.driver.maximize_window()

    def test_key_ui_elements(self):
        driver = self.driver

        # Verify header elements
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.header-area')))
        
        # Verify navigation links
        nav_links = driver.find_elements(By.CSS_SELECTOR, '.main-menu nav ul li a')
        expected_links = ['Home', 'Tables', 'Chairs']
        visible_links = [link.text for link in nav_links if link.is_displayed()]
        for link in expected_links:
            self.assertIn(link, visible_links, f'{link} link is not visible in navigation.')

        # Verify form fields
        login_tab = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.nav-link[aria-selected="false"]')))
        login_tab.click()

        login_form = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.login-register-form')))
        input_fields = login_form.find_elements(By.CSS_SELECTOR, 'input')
        self.assertGreaterEqual(len(input_fields), 2, 'Not all input fields are present.')

        # Verify buttons
        buttons = login_form.find_elements(By.CSS_SELECTOR, 'button')
        self.assertTrue(any(button.is_displayed() for button in buttons), 'No buttons are visible.')

        # Interact with Accept Cookies button
        accept_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'rcc-confirm-button')))
        accept_button.click()

        # Verify the UI updates visually
        try:
            WebDriverWait(driver, 5).until_not(EC.visibility_of_element_located((By.ID, 'rcc-confirm-button')))
        except:
            self.fail("Cookies consent button didn't disappear after clicking.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()