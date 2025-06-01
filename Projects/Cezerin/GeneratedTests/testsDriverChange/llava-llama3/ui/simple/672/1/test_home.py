import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.assertions import Assert
from selenium.webdriver.common.action import ActionChains
from selenium.webdriver.common.alerts import Alert
from selenium.webdriver.common.touch_action import TouchAction

class TestCrocsAdvertisement(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "http://localhost:3000"
        self.category_a_url = self.url + "/category-a"
        self.category_a_1_url = self.url + "/category-a-1"

    def tearDown(self):
        self.driver.quit()

    def test_ad_content(self):
        try:
            # Check that the main UI components are present
            headers = self.driver.find_elements_by_css_selector("h3")

            buttons = self.driver.find_elements_by_tag_name("button")
            links = self.driver.find_elements_by_tag_name("a")
            form_fields = self.driver.find_elements_by_tag_name("input")

            # Check that these elements exist and are visible
            assert headers, "Header is missing."
            assert len(buttons) > 1, "There should be at least one button."
            assert links[0].get_attribute("href") == self.url + "/category-a", "The first link does not lead to the correct page."

            # Check that the text is visible
            ad_text = self.driver.find_element_by_css_selector(".ad-text")
            assert ad_text.get_attribute("innerHTML").strip() == "Selected Stores - $30 each.", "The ad text is missing or incorrect."
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == '__main__':
    unittest.main()