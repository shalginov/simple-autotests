from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_add_to_cart(browser, base_url):
    browser.get(base_url)
    wait = WebDriverWait(browser, 1)
    actions = ActionChains(browser)

    button_add_to_cart = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"content\"]/div[2]/div[1]/div/div[2]/form/div/button[1]")))
    actions.move_to_element(button_add_to_cart).click().perform()

    button_dropdown_cart = browser.find_element(By.CSS_SELECTOR, "button[data-bs-toggle=\"dropdown\"]")
    actions.move_to_element(button_dropdown_cart).click().perform()
    button_go_to_cart = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "View Cart")))
    actions.move_to_element(button_go_to_cart).click().perform()
    assert wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*[@id=\"shopping-cart\"]/div/table/tbody/tr/td[3]"), "Product 16"))
