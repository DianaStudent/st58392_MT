import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestWebPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_ui_elements(self):
        driver = self.driver

        # Wait for the main elements to load
        wait = WebDriverWait(driver, 20)

        # Confirm the presence of key navigation links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.ID, "index")))
            clothes_link = driver.find_element(By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']")
            accessories_link = driver.find_element(By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']")
            art_link = driver.find_element(By.XPATH, "//a[@href='http://localhost:8080/en/9-art']")
            login_link = driver.find_element(By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F']")
            register_link = driver.find_element(By.XPATH, "//a[@href='http://localhost:8080/en/registration']")
        except:
            self.fail("Some navigation links are missing or not visible")

        # Confirm the presence of key interface elements
        try:
            banner = wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@src='http://localhost:8080/modules/ps_banner/img/sale70.png']")))
            search_input = driver.find_element(By.XPATH, "//input[@placeholder='Search our catalog']")
            subscribe_button = driver.find_element(By.XPATH, "//input[@value='Subscribe']")
        except:
            self.fail("Some key interface elements are missing or not visible")

        # Interact with search input
        try:
            search_input.click()
            search_input.send_keys("Test Product")
            submit_button = driver.find_element(By.XPATH, "//i[@class='material-icons search']")
            submit_button.click()

            # Ensure no errors occur
            current_url = driver.current_url
            self.assertNotIn("error", current_url.lower())
        except:
            self.fail("Interaction with search input caused errors")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()