from enum import Enum


class WebElementType(Enum):
    Element = 0
    Text = 1
    Link = 2
    TextBox = 3
    Button = 4
    CheckBox = 5


class ElementSelector:
    by = None
    element_type = None
    text = None

    def __init__(self, by, type, text=None):
        self.by = by
        self.element_type = type
        self.text = text

    def get_text(self):
        return self.text

    def get_by(self):
        return self.by

    def get_type(self):
        return self.element_type

    # def add_to_end(self, addon):
    #     return ''.join([str(self.by), str(addon)])
    #
    # def add_by(self, addon):
    #     return ElementSelector(by=str(self.get_by()).format(str(addon)), type=self.get_type(), text=self.get_text())