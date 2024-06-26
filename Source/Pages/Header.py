
from myvenv6.ssqatest.src.SeleniumExtended import SeleniumExtended
from myvenv6.ssqatest.src.pages.locators.HeaderLocator import HeaderLocator

class Header(HeaderLocator):

    def __init__(self,driver):
        self.driver=driver
        self.sl=SeleniumExtended(self.driver)

    def click_on_cart_on_right_header(self):
        self.sl.wait_and_click(self.CART_RIGHT_BTN)

    def wait_untill_cart_item_count(self,count):
        expected_text=str(count)+' item'
        self.sl.wait_until_element_contains_text(self.CART_ITEM_COUNT,expected_text)
