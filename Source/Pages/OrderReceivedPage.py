
from myvenv6.ssqatest.src.SeleniumExtended import SeleniumExtended
from myvenv6.ssqatest.src.pages.locators.OrderReceivedPageLocators import OrderReceivedPageLocators


class OrderReceivedPage(OrderReceivedPageLocators):


    def __init__(self,driver):
        self.driver=driver
        self.sl=SeleniumExtended(self.driver)

    def verify_order_received_page_loaded(self):
        self.sl.wait_until_element_contains_text(self.PAGE_MAIN_HEADER,"Order received")
        print(self.driver.title)
