from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestUIProcess(unittest.TestCase):

    def setUp(self):
        # Setup Chrome WebDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_page_elements(self):
        driver = self.driver
        wait = self.wait

        # Check header visibility
        header = wait.until(EC.visibility_of_element_located((By.ID, 'header')))
        self.assertTrue(header.is_displayed(), "Header is not visible")

        # Check footer visibility
        footer = wait.until(EC.visibility_of_element_located((By.ID, 'footer')))
        self.assertTrue(footer.is_displayed(), "Footer is not visible")

        # Check navigation visibility
        nav = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header-nav')))
        self.assertTrue(nav.is_displayed(), "Navigation is not visible")

        # Check input fields, buttons, labels, sections
        search_input = wait.until(EC.visibility_of_element_located((By.NAME, 's')))
        self.assertTrue(search_input.is_displayed(), "Search input is not visible")

        login_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F']")))
        self.assertTrue(login_button.is_displayed(), "Login button is not visible")

        register_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/registration']")))
        self.assertTrue(register_link.is_displayed(), "Register link is not visible")

        # Interact with button and confirm UI reaction
        login_button.click()
        new_url = "http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F"
        self.assertEqual(driver.current_url, new_url, "Did not navigate to login page after clicking login button")

        # Assert main UI components
        components = [
            ("Header", header),
            ("Footer", footer),
            ("Navigation", nav),
            ("Search input", search_input),
            ("Login button", login_button),
            ("Register link", register_link)
        ]

        for name, component in components:
            if not component.is_displayed():
                self.fail(f"{name} is not visible or missing")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()