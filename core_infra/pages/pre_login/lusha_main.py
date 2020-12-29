
import allure

from core_infra.elements.selector import ElementSelector, WebElementType
from core_infra.pages.pre_login.base_pre_login import BasePreLogin



class MainPage(BasePreLogin):
    url = 'https://www.lusha.com/'
    hero_center = ElementSelector(".hero__center", WebElementType.Element)

    def __init__(self, browser):
        super().__init__(browser)

    def validate_page(self):
        with allure.step('Validating page Main Page'):
            self.wait_visible(selector=self.hero_center, max_wait=10)
            super().validate_page()


