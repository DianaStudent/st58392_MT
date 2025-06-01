from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class WebsiteUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/3-clothes")

    def test_ui_elements(self):
        driver = self.driver

        try:
            # Wait for page to load and check elements
            wait = WebDriverWait(driver, 20)

            # Verify header links
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']")))
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']")))
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']")))

            # Verify login link
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art']")))

            # Verify register link
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/registration']")))

            # Verify main banner
            wait.until(EC.visibility_of_element_located((By.ID, "category")))

            # Verify search input
            wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search our catalog']")))

            # Interact: Click on 'Clothes' link and ensure no errors
            clothes_link = driver.find_element(By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']")
            clothes_link.click()

            # Confirm the page updates with no errors (still loaded correctly)
            wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "Clothes"))

        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()