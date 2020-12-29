import unittest
from selenium import webdriver


class BaseBrowser(unittest.TestCase):
    browser = None

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    @classmethod
    def setUp(cls):
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("start-maximized")  # open Browser in maximized mode
        chrome_options.add_argument("disable-infobars")  # disabling infobars
        chrome_options.add_argument("--disable-extensions")  # disabling extensions
        chrome_options.add_argument("--disable-dev-shm-usage")  # overcome limited resource problems
        chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
        try:
            cls.browser = webdriver.Chrome(options=chrome_options)
        except:
            pass
        if not cls.browser:
            raise unittest.SkipTest('Web browser not available')

    @classmethod
    def tearDown(cls):
        if cls.browser:
            cls.browser.close()
