from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestYourCommerce(unittest.TestCase):
    def setUp(self):
        # Set up the WebDriver and navigate to the home page.
        driver = webdriver.Chrome(ChromeDriverManager().get_chrome_driver())
        self.driver = driver
        self.driver.get("http://max/")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='header-link'][@href='login']")))

    def tearDown(self):
        # Close the WebDriver.
        self.driver.quit()

    def test_search_page(self):
        # Navigate to the search page and confirm its presence.
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='header-link'][@href='search']"))))
        self.assertEqual(self.driver.current_url,
                         "http://max/search")

if __name__ == '__main__':
    unittest.main()