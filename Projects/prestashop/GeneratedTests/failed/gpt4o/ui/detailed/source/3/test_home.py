from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestDemoUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/en/")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except:
            self.fail("Header is missing or not visible.")

        # Check footer
        try:
            footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        except:
            self.fail("Footer is missing or not visible.")

        # Check navigation links
        navigation_links = [
            "http://localhost:8080/en/3-clothes",
            "http://localhost:8080/en/6-accessories",
            "http://localhost:8080/en/9-art"
        ]
        for link in navigation_links:
            try:
                nav_element = driver.find_element(By.XPATH, f"//a[@href='{link}']")
                self.assertTrue(nav_element.is_displayed(), f"Navigation link {link} is not visible.")
            except:
                self.fail(f"Navigation link {link} is missing.")

        # Check presence of login and register links
        try:
            login_link = driver.find_element(By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art']")
            self.assertTrue(login_link.is_displayed(), "Login link is not visible.")
        except:
            self.fail("Login link is missing.")

        try:
            register_link = driver.find_element(By.XPATH, "//a[@href='http://localhost:8080/en/registration']")
            self.assertTrue(register_link.is_displayed(), "Register link is not visible.")
        except:
            self.fail("Register link is missing.")

        # Check search bar visibility
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.NAME, "s")))
        except:
            self.fail("Search input is missing or not visible.")

        # Check buttons such as cart and wishlist
        button_ids = ["_desktop_cart", "_desktop_user_info"]
        for button_id in button_ids:
            try:
                button = driver.find_element(By.ID, button_id)
                self.assertTrue(button.is_displayed(), f"Button with ID {button_id} is not visible.")
            except:
                self.fail(f"Button with ID {button_id} is missing.")

        # Check interaction with the search input
        try:
            search_input.send_keys("Test Product")
            search_button = driver.find_element(By.XPATH, "//button[@type='submit' and @name='submitNewsletter']")
            search_button.click()
        except:
            self.fail("Failed to interact with the search functionality.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()