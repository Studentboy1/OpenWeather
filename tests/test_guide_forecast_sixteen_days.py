from pages.main_page import MainPage
from pages.login_page import LoginPage

def test_guest_can_go_to_guide_forecast_sixteen_days(browser):
    url = "https://openweathermap.org/guide"
    page = MainPage(browser, url)
    page.open()
    page.go_to_guide_forecast_sixteen_days()
    login_page = LoginPage(browser, browser.current_url)
    login_page.test_current_url_guide_forecast_sixteen_days()