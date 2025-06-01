import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIElements(unittest.TestCase):

    def setUp(self):
        # Setup Chrome WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/login")

    def test_ui_elements_presence(self):
        driver = self.driver

        try:
            # Verify the logo is present
            logo = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.logo a img"))
            )

            # Verify the navigation links are present
            nav_links = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.main-menu nav ul"))
            )

            # Check 'Home' link
            home_link = nav_links.find_element(By.LINK_TEXT, "Home")
            self.assertTrue(home_link.is_displayed())

            # Check 'Tables' link
            tables_link = nav_links.find_element(By.LINK_TEXT, "Tables")
            self.assertTrue(tables_link.is_displayed())

            # Check 'Chairs' link
            chairs_link = nav_links.find_element(By.LINK_TEXT, "Chairs")
            self.assertTrue(chairs_link.is_displayed())

            # Verify the Login/Register tab is present
            login_tab = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='#'][data-rb-event-key='login']"))
            )
            register_tab = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='#'][data-rb-event-key='register']"))
            )

            # Verify the forms are present
            email_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "email"))
            )
            password_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "password"))
            )
            repeat_password_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "repeatPassword"))
            )
            first_name_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "firstName"))
            )
            last_name_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "lastName"))
            )
            state_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "stateProvince"))
            )
            country_select = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "select"))
            )
            register_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.button-box [type='submit']"))
            )

        except Exception as e:
            self.fail(f"Failed during test: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()