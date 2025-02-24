from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_register_account(browser):
    browser.get("http://192.168.27.17:8081/en-gb?route=account/register")
    wait = WebDriverWait(browser, 2, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.ID, "input-firstname")))
    wait.until(EC.visibility_of_element_located((By.ID, "input-lastname")))
    wait.until(EC.visibility_of_element_located((By.ID, "input-email")))
    wait.until(EC.visibility_of_element_located((By.ID, "input-password")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))