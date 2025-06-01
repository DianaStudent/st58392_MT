import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

class TestRegistrationPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://max/register?returnUrl=/")

    def tearDown(self):
        self.driver.quit()

    def test_register_page_elements_present(self):
        try:
            # Check that the main UI components are present
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_css_selector(".header"))
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_css_selector(".title"))

            # Verify the presence of key interface elements: navigation links, inputs, buttons, banners
            self.assertTrue(self.driver.find_elements_by_css_selector("nav ul li")[2].text == "Login")
            self.assertTrue(self.driver.find_elements_by_css_selector("nav ul li")[3].text == "Forgot Password")
            self.assertTrue(self.driver.find_elements_by_css_selector("form fieldset")[0])

            # Check that these elements exist and are visible
            self.assertTrue(self.driver.find_element_by_css_selector("header .logo").is_displayed)
            self.assertTrue(self.driver.find_elements_by_css_selector("nav ul li")[2].is_displayed)
            self.assertTrue(self.driver.find_elements_by_css_selector("nav ul li")[3].is_displayed)
            self.assertTrue(self.driver.find_elements_by_css_selector("form fieldset")[0].is_displayed)

        except:
            self.fail()

    def test_register_page_elements_interaction(self):
        try:
            # Confirm the presence of key interface elements: navigation links, inputs, buttons, banners
            WebDriverWait(self.driver, 20).until(lambda x: x.find_element_by_css_selector(".header"))
            WebDriverWait(self.driver, 20).until(lambda x: x.find_elements_by_css_selector("nav ul li")[0].is_displayed)
            WebDriverWait(self.driver, 20).until(lambda x: x.find_elements_by_css_selector("form fieldset")[1])

            # Interact with one or two elements
            self.driver.find_element_by_css_selector("form fieldset")[1].find_element_by_name("email").send_keys("test@email.com")
            self.assertEqual(self.driver.find_element_by_css_selector("form fieldset")[1].find_element_by_name("email").get_attribute("value"), "test@email.com")

        except:
            self.fail()

if __name__ == "__main__":
    unittest.main()