from enum import Enum

import allure

from core_infra.elements.selector import ElementSelector, WebElementType
from core_infra.pages.base_page import BasePage


class BasePreLogin(BasePage):
    url = 'https://www.lusha.com/'
    logo = ElementSelector("#logo", WebElementType.Button)
    login = ElementSelector(".login", WebElementType.Button, 'Login')
    header_top_company = ElementSelector('#nav-item-2066', WebElementType.Button, 'Company')
    header_top_company_about = ElementSelector('#nav-item-8121', WebElementType.Button, 'About')

    def __init__(self, browser):
        super().__init__(browser)

    ###########################################
    #######  base pre login functions  ########
    ###########################################
    def click_login(self):
        with allure.step('clicking login button'):
            self.click(self.login)

    def validate_page(self):
        with allure.step('Validating page BasePreLogin Page'):
            self.validate_text(selector=self.login, max_try=3)
            self.validate_url()
            super().validate_page()

    def click_about(self):
        self.hover(selector=self.header_top_company)
        self.click(selector=self.header_top_company_about)
        pass

class TopHeader(Enum):
    Element = 0
    Text = 1
    Link = 2
    TextBox = 3
    Button = 4
    CheckBox = 5


