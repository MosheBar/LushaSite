import allure
from core_infra.elements.selector import ElementSelector, WebElementType
from core_infra.pages.pre_login.base_pre_login import BasePreLogin


class AboutPage(BasePreLogin):
    url = 'https://www.lusha.com/about/'
    hero = ElementSelector(".hero-videoBg", WebElementType.Element)
    ourTeam = ElementSelector("#ourTeam", WebElementType.Element)
    cards = [{'name': 'Assaf Eisenstein', 'title': 'Co-Founder & President', 'quote': '“Who dares, wins.”'},
             {'name': 'Yoni Tserruya', 'title': 'Co-Founder & CEO',
              'quote': '“Everything you want waits on the other side of consistency.”'},
             {'name': 'Lior Berger', 'title': 'Advisory Board Member',
              'quote': '“Unleashing the power of entrepreneurship...”'},
             {'name': 'Rachel Haim', 'title': 'VP Product', 'quote': '“Greatness. Nothing less.”'},
             {'name': 'Rachel Shani Stopper', 'title': 'VP HR', 'quote': '“Be positive, the rest will follow.”'},
             {'name': 'Chen Guter', 'title': 'VP Marketing', 'quote': '“Some people want it to happen, others make it happen."'},
             {'name': 'Shai Gottesdiener', 'title': 'VP R&D', 'quote': '“With data comes power. With power comes responsibility."'}]
    cards_element = ElementSelector(".our-team__member", WebElementType.Element)
    card_name = ElementSelector(".mb-0", WebElementType.Text)
    card_title = ElementSelector(".mb-3", WebElementType.Text)
    card_quote = ElementSelector(".our-team__quate", WebElementType.Text)

    def __init__(self, browser):
        super().__init__(browser)

    def validate_page(self):
        with allure.step('Validating page Main Page'):
            self.wait_visible(selector=self.hero, max_wait=10)
            super().validate_page()

    def go_our_team(self):
        with allure.step('go to Our team section'):
            self.move_to_element(selector=self.ourTeam)

    def validate_cards(self):
        with allure.step('validating all cards in our team'):
            web_cards = self.get_elements(selector=self.cards_element)

            with allure.step('validating number of cards'):
                self.iAssert.equal(len(web_cards), len(self.cards), 'failed to compare number of cards')

            loc = 0
            for card in self.cards:
                name = card.get('name')
                title = card.get('title')
                quote = card.get('quote')
                with allure.step(' '.join(['validating card for name:', str(name), ', title: ', str(title),
                                           ', with quote: ', str(quote)])):
                    self.iAssert.equal(web_cards[loc].text, '\n'.join([str(name), str(title), str(quote)]))
                    loc += 1




