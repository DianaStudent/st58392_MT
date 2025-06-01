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
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/3-clothes")

    def test_ui_elements(self):
        driver = self.driver

        try:
            # Verify the presence of navigational links
            home_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="http://localhost:8080/en/"]'))
            )

            clothes_link = driver.find_element(By.CSS_SELECTOR, 'a[href="http://localhost:8080/en/3-clothes"]')
            accessories_link = driver.find_element(By.CSS_SELECTOR, 'a[href="http://localhost:8080/en/6-accessories"]')
            art_link = driver.find_element(By.CSS_SELECTOR, 'a[href="http://localhost:8080/en/9-art"]')
            login_link = driver.find_element(By.CSS_SELECTOR, 'a[href="http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art"]')
            register_link = driver.find_element(By.CSS_SELECTOR, 'a[href="http://localhost:8080/en/registration"]')

            # Verify presence of input fields and buttons
            search_input = driver.find_element(By.CSS_SELECTOR, 'input[name="s"]')
            subscribe_input = driver.find_element(By.CSS_SELECTOR, 'input[name="email"]')
            subscribe_button = driver.find_element(By.CSS_SELECTOR, 'input[name="submitNewsletter"]')

            # Verify presence of banners
            header_banner = driver.find_element(By.CLASS_NAME, 'header-banner')

            # Interact with some elements and verify updates
            if not home_link.is_displayed() or not clothes_link.is_displayed():
                self.fail("Critical navigation links are not visible.")

            # Click on clothes link and verify it opens correctly
            clothes_link.click()
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Clothes')]"))
            )

            # Click on login link and verify it opens the login page
            login_link.click()
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Login')]"))
            )

            # Verify no unexpected errors are caused
            console_logs = driver.get_log('browser')
            for log in console_logs:
                if log['level'] == 'SEVERE':
                    self.fail(f"UI caused severe error: {log['message']}")

        except Exception as e:
            self.fail(f"Test failed due to exception: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()