import allure
import pytest
from core_infra.elements.base_browser import BaseBrowser
from core_infra.pages.pre_login.about import AboutPage
from core_infra.pages.pre_login.lusha_main import MainPage


class LushaTest(BaseBrowser):
    @classmethod
    # @pytest.mark.skip
    def test_about_cards(cls):
        with allure.step('Visit Lusha website'):
            main_page = MainPage(cls.browser)
            main_page.navigate(main_page.url)
            main_page.validate_page()

        with allure.step('Navigate to about page'):
            main_page.click_about()

        with allure.step('Analyze the data'):
            about_page = AboutPage(cls.browser)
            about_page.validate_page()
            about_page.go_our_team()
            about_page.validate_cards()


