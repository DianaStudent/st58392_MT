import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class TestShopReactApp(unittest.TestCase):

    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def tearDown(self):
        self.driver.quit()

    def test_shop_react_app(self):
        self.driver.get('http://localhost/')

        # Confirm the presence of key interface elements: navigation links, inputs, buttons, banners.
        self._check_navigation_links()
        self._check_form_fields()
        self._check_buttons()
        self._check_banners()

        # Interact with one or two elements — e.g., click a button and check that the UI updates visually.
        self._click_button('button')

        # Verify that interactive elements do not cause errors in the UI.
        self.driver.implicitly_wait(10)

    def _check_navigation_links(self):
        navigation_links = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'nav ul li a'))
        )
        if len(navigation_links) != 4:
            self.fail('Navigation links are missing')

    def _check_form_fields(self):
        form_fields = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, 'input'))
        )
        if len(form_fields) < 2:
            self.fail('Form fields are missing')

    def _check_buttons(self):
        buttons = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, 'button'))
        )
        if len(buttons) != 2:
            self.fail('Buttons are missing')

    def _check_banners(self):
        banners = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#banner'))
        )
        if not banners.is_displayed():
            self.fail('Banner is hidden')

    def _click_button(self, button_id):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, button_id))
            ).click()
        except TimeoutException:
            self.fail(f'Button with id {button_id} is not found')
        except NoSuchElementException:
            self.fail(f'Button with id {button_id} is missing')

if __name__ == '__main__':
    unittest.main()