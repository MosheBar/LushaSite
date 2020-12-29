import allure
from asserts import *


class Assert:
    def equal(self, a, b, free_text=None):
        with allure.step("assert equal between: " + str(a) + " with: " + str(b)):
            assert_equal(a, b, "failed to compare equal " + str(free_text) if free_text else '')

    def not_equal(self, a, b, free_text=None):
        with allure.step("assert not equal between: " + str(a) + " with: " + str(b)):
            assert_not_equal(a, b, "failed to compare not equal " + str(free_text) if free_text else '')

    def greater(self, a, b, free_text=None):
        with allure.step("assert greater between: " + str(a) + " with: " + str(b)):
            assert_greater(a, b, "failed to compare Greater " + str(free_text) if free_text else '')

    def less(self, a, b, free_text=None):
        with allure.step("assert less between: " + str(a) + " with: " + str(b)):
            assert_less(a, b, "failed to compare less " + str(free_text) if free_text else '')

    def assert_in(self, a, b, free_text=None):
        with allure.step("assert in between: " + str(a) + " with: " + str(b)):
            assert_in(a, b, "failed to validate in between " + str(free_text) if free_text else '')

    def assert_not_in(self, a, b, free_text=None):
        with allure.step("assert not in between: " + str(a) + " with: " + str(b)):
            assert_not_in(a, b, "failed to validate not in between " + str(free_text) if free_text else '')

    def assert_contain(self, a, b, free_text=None):
        with allure.step("assert contain between: " + str(a) + " with: " + str(b)):
            assert_true(a in b, "failed to validate in between " + str(free_text) if free_text else '')

    def assert_not_contain(self, a, b, free_text=None):
        with allure.step("assert not contain between: " + str(a) + " with: " + str(b)):
            assert_true(a not in b, "failed to validate not in between " + str(free_text) if free_text else '')

    def assert_true(self, expected, free_text=None):
        with allure.step("assert True and got: " + str(expected)):
            assert_true(expected, "failed to validate expected to be True " + str(free_text) if free_text else '')