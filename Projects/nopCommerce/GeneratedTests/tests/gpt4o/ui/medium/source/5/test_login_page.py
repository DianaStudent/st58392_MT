import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/login?returnUrl=%2F")

    def test_ui_elements(self):
        driver = self.driver

        try:
            # Verify navigation links
            nav_links = ["Home page", "New products", "Search", "My account", "Blog", "Contact us"]
            for link_text in nav_links:
                nav_link = WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.LINK_TEXT, link_text))
                )
                self.assertTrue(nav_link.is_displayed(), f"Navigation link {link_text} is not visible")

            # Verify form fields and buttons
            form_elements = {
                "Email": (By.ID, "Email"),
                "Password": (By.ID, "Password"),
                "Register": (By.CSS_SELECTOR, "button.register-button"),
                "Log in": (By.CSS_SELECTOR, "button.login-button")
            }
            for elem_name, locator in form_elements.items():
                element = WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located(locator)
                )
                self.assertTrue(element.is_displayed(), f"{elem_name} is not visible")

            # Interact with search box and check for alert
            search_box = driver.find_element(By.ID, "small-searchterms")
            search_button = driver.find_element(By.CSS_SELECTOR, "button.search-box-button")
            search_box.clear()
            search_button.click()
            alert = driver.switch_to.alert
            self.assertEqual(alert.text, 'Please enter some search keyword')

            alert.accept()

        except Exception as e:
            self.fail(f"Test failed with exception: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()