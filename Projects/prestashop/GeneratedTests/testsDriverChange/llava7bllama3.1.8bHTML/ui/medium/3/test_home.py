import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        self.driver.get("http://localhost:8080/en/")

        # Navigation links
        navigation_links = self.driver.find_element(By.XPATH, "//ul[@class='sf-menu sf-js-enabled']")
        self.assertTrue(navigation_links.is_displayed())

        # Inputs
        search_input = self.driver.find_element(By.NAME, "search_query")
        self.assertTrue(search_input.is_enabled())
        self.assertTrue(search_input.is_displayed())

        # Buttons
        submit_button = self.driver.find_element(By.NAME, "submit_search")
        self.assertTrue(submit_button.is_enabled())
        self.assertTrue(submit_button.is_displayed())

        # Banners
        banner_image = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//img[@class='banner']")))
        self.assertTrue(banner_image.is_displayed())

        # Interact with button and verify UI update
        submit_button.click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='message success']")))

    def test_ui_interactivity(self):
        self.driver.get("http://localhost:8080/en/")

        # Click on banner image and verify no error
        banner_image = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//img[@class='banner']")))
        banner_image.click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='message success']")))

if __name__ == "__main__":
    unittest.main()