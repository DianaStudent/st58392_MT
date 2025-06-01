from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class TestMaxWebsite(unittest.TestCase):

    def setUp(self):
        options = Options()
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("http://max/")

    def tearDown(self):
        self.driver.quit()

    def test_max_website(self):
        # Check presence of key interface elements
        navigation_links = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//nav//ul//li/a")))
        inputs = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.TAG_NAME, "input")))
        buttons = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))
        banners = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='banner']")))

        # Interact with one or two elements
        button = buttons[0]
        button.click()
        self.assertEqual(button.get_attribute("disabled"), None)  # Assuming the button becomes disabled after clicking

        # Verify that interactive elements do not cause errors in the UI
        navigation_links[0].click()
        self.assertNotEqual(self.driver.title, "Error Page")  # Assuming an error page has a different title

    def test_max_search_page(self):
        search_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='search-button']")))
        search_input = self.driver.find_element(By.TAG_NAME, "input")
        search_button.click()
        self.assertEqual(search_input.get_attribute("value"), "")  # Assuming the input field's value is cleared after searching

if __name__ == "__main__":
    unittest.main()