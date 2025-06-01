import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestPage(unittest.TestCase):

    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://example.com")  # replace with your URL

    def test_main_ui_components(self):
        # Check that the main UI components are present: headers, buttons, links, form fields, etc.
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#nav")))

        self.failUnlessElementVisible("#nav")
        self.failUnlessElementVisible("#home")

    def test_navigation_links(self):
        # Check that navigation links are present and work
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#category_a")))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/category_a']")))

        category_a_link = self.driver.find_element_by_xpath("//a[@href='/category_a']")
        category_a_link.click()

    def test_inputs_buttons_banners(self):
        # Check that inputs, buttons and banners are present and work
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@type='text']")))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))

        banner = self.driver.find_element_by_css_selector("#banner")
        banner.click()

    def failUnlessElementVisible(selector):
        element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
        self.assertTrue(element.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()