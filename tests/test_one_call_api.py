from pages.main_page import MainPage
from pages.login_page import LoginPage

def test_guest_can_go_to_one_call_api(browser):
    url = "https://openweathermap.org/"
    page = MainPage(browser, url)
    page.open()
    page.go_to_one_call_api()
    login_page = LoginPage(browser, browser.current_url)
    login_page.test_current_url_one_call_api()