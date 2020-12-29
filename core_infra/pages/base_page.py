import time

import allure
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from core_infra.elements.selector import ElementSelector, WebElementType
from core_infra.service.validation import Assert
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    iAssert = None
    browser = None
    page_title = ElementSelector(None, WebElementType.Text, 'NeedToSetPageTitle')
    url = 'https://www.lusha.com/'

    def __init__(self, browser):
        self.browser = browser
        self.iAssert = Assert()

    #################################
    #######  base functions  ########
    #################################

    def click(self, selector):
        with allure.step('clicking selector'):
            self.wait_exist(selector)
            self.browser.find_element_by_css_selector(selector.get_by()).click()

    def hover(self, selector):
        with allure.step('hover selector'):
            self.wait_exist(selector)
            hov = ActionChains(self.browser).move_to_element(self.browser.find_element_by_css_selector(selector.get_by()))
            hov.perform()

    def navigate(self, url):
        with allure.step("navigating to url: " + str(url)):
            self.browser.get(url)

    def wait_exist(self, selector, max_wait=3):
        with allure.step('waiting max of {} seconds until selector: "{}" appears'.format(str(max_wait),
                                                                                         str(selector.get_by()))):
            wait = WebDriverWait(self.browser, max_wait)
            wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, selector.get_by())))

    def wait_visible(self, selector, max_wait=3):
        with allure.step('waiting max of {} seconds until selector: "{}" appears'.format(str(max_wait),
                                                                                         str(selector.get_by()))):
            wait = WebDriverWait(driver=self.browser, timeout=max_wait)
            wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, selector.get_by())))

    #################################
    #######  page functions  ########
    #################################

    def get_element(self, selector, get_father=False):
        element = self.browser.find_element_by_css_selector(selector.get_by())
        if get_father:
            element = element.find_element_by_xpath('..')
        return element

    def get_elements(self, selector):
        return self.browser.find_elements_by_css_selector(selector.get_by())

    def get_text(self, selector, attr=None, get_father=False):
        if attr:
            return self.browser.find_element_by_css_selector(selector.get_by()).get_attribute(attr)
        else:
            return self.get_element(selector, get_father=get_father).text

    def set_text(self, selector, text=None, clear=True):
        with allure.step('setting text: ' + str(text) if text else 'no text input!'):
            if text:
                if clear:
                    self.browser.find_element_by_css_selector(selector.get_by()).clear()
                self.browser.find_element_by_css_selector(selector.get_by()).send_keys(text)

    def move_to_element(self, selector):
        with allure.step('move to element'):
            element = self.browser.find_element_by_css_selector(selector.get_by())
            self.browser.execute_script("arguments[0].scrollIntoView();", element)

    #####################################
    #######  validate functions  ########
    #####################################

    def validate_page(self):
        pass

    def validate_title(self):
        with allure.step("validating title page"):
            max_try = 3
            while max_try > 0:
                try:
                    self.iAssert.equal(self.browser.title, self.page_title.get_text())
                    return
                except AssertionError:
                    max_try -= 1
            self.iAssert.equal(self.browser.title, self.page_title.get_text())

    def validate_url(self):
        with allure.step('validating URL'):
            self.iAssert.equal(self.url, self.browser.current_url)

    def validate_text(self, selector, attr=None, get_father=False, expected_text=None, max_try=1):
        current_text = None
        while max_try > 0:
            try:
                if expected_text is None:
                    expected_text = selector.get_text()
                self.wait_exist(selector)
                current_text = self.get_text(selector, attr=attr, get_father=get_father)
                self.iAssert.equal(expected_text, current_text)
                max_try = 0
            except (AssertionError, NoSuchElementException, TimeoutException):
                time.sleep(1)
                max_try -= 1
        self.iAssert.equal(expected_text, current_text)