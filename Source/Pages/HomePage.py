from myvenv6.ssqatest.src.SeleniumExtended import SeleniumExtended
from myvenv6.ssqatest.src.pages.locators.HomePageLocators import HomePageLocators

class HomePage(HomePageLocators):

    def __init__(self,driver):
        self.driver=driver
        self.sl=SeleniumExtended(self.driver)

    def go_to_my_page(self):
        home_url='http://demostore.supersqa.com/'
        self.driver.get(home_url)
        self.driver.maximize_window()

    def click_first_add_to_cart_button(self):
        self.sl.wait_and_click(self.ADD_TO_CART_BTN)
