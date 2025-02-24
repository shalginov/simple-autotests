import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


@pytest.mark.parametrize("currency, sign", [("Euro", "€"), ("Pound Sterling", "£"), ("US Dollar", "$")])
def test_change_currency(browser, base_url, currency, sign):
    browser.get(base_url)
    wait = WebDriverWait(browser, 1)
    actions = ActionChains(browser)

    form_dropdown_currencies = wait.until(EC.visibility_of_element_located((By.ID, "form-currency")))
    actions.move_to_element(form_dropdown_currencies).click().perform()
    link_euro = browser.find_element(By.PARTIAL_LINK_TEXT, currency)
    actions.move_to_element(link_euro).click().perform()
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//*[@id=\"form-currency\"]/div/a/strong"),sign))

    def check_prices():
        for cl in ("price-new", "price-old", "price-tax"):
            prices = browser.find_elements(By.CSS_SELECTOR, cl)
            if prices:
                for price in prices:
                    assert sign in price.text
            else:
                NoSuchElementException("No prices has located")

    check_prices()

    browser.find_element(By.LINK_TEXT, "Cameras").click()
    check_prices()
