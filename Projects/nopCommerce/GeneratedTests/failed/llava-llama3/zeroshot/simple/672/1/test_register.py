from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

def setUp(self):
self.driver = webdriver.Chrome(options=Options())
self.email = f"test{str(uuid.uuid4())}@test.com"
self.password = "test11"

def tearDown(self):
self.driver.quit()

class TestRegisterSimpleProcess(unittest.TestCase):
def test_register_simple_process(self):
driver_path = '/path/to/chromedriver'
options = Options()
options.add_argument('--headless')
options.add_argument('--window-size=1920x1080')
options.add_argument('start-maximized')
options.add_argument(f'--user-data-dir=/path/to/user-data-dir')
options.add_argument('no-sandbox')

driver = webdriver.Chrome(options=options)

try:
# Go to the registration page
register_page = driver.get('http://max/register')

assert register_page, "Failed to open registration page"

# Fill out personal details
first_name_input = register_page.find_element_by_name('FirstName')
first_name_input.send_keys('First Name')
last_name_input = register_page.find_element_by_name('LastName')
last_name_input.send_keys('Last Name')

# Select newsletter option
newsletter_checkbox = register_page.find_element_by_name('Newsletter')
assert newsletter_checkbox.is_selected(), "Failed to select newsletter"

password_input = register_page.find_element_by_name('Password')
password_input.send_keys(self.password)

confirm_password_input = register_page.find_element_by_name('ConfirmPassword')
confirm_password_input.send_keys(self.password)

# Submit the registration form
register_button = register_page.find_element_by_name('register-button')
register_button.click()

# Wait for confirmation page to open
confirm_page = WebDriverWait(driver, 20).until(
ecaise_of(
lambda x: 'Your registration completed' in x.page_source)
)

assert confirm_page, "Failed to confirm registration"

except Exception as e:
self.fail(str(e))

if __name__ == '__main__':
unittest.main()