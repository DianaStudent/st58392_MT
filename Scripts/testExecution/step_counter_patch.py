from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait

step_counter = {"count": 0}
_original_click = WebElement.click
def patched_click(self):
    step_counter["count"] += 1
    print("STEP")
    return _original_click(self)
WebElement.click = patched_click
_original_send_keys = WebElement.send_keys
def patched_send_keys(self, *args, **kwargs):
    step_counter["count"] += 1
    print("STEP")
    return _original_send_keys(self, *args, **kwargs)
WebElement.send_keys = patched_send_keys
_original_until = WebDriverWait.until
def patched_until(self, method, message=''):
    step_counter["count"] += 1
    print("STEP")
    return _original_until(self, method, message)
WebDriverWait.until = patched_until
