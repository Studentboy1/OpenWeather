from pages.main_page import MainPage
from pages.login_page import LoginPage

def test_guest_can_go_to_guide_history_achive_46_years(browser):
    url = "https://openweathermap.org/guide"
    page = MainPage(browser, url)
    page.open()
    page.go_to_guide_history_achive_46_years()
    login_page = LoginPage(browser, browser.current_url)
    login_page.test_current_url_guide_history_achive_46_years()