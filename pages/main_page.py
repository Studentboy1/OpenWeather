import time
from base.base_class import BasePage
from locators.locator import MainPageLocators
from pages.login_page import LoginPage
from selenium.webdriver.common.keys import Keys

class MainPage(BasePage):
    def go_to_guide(self):
        self.browser.maximize_window()
        click_guide = self.browser.find_element(*MainPageLocators.guide)
        click_guide.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_api(self):
        self.browser.maximize_window()
        click_api = self.browser.find_element(*MainPageLocators.api)
        click_api.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_dashboard(self):
        self.browser.maximize_window()
        click_dashboard = self.browser.find_element(*MainPageLocators.dashboard)
        click_dashboard.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_marketplace(self):
        self.browser.maximize_window()
        click_market = self.browser.find_element(*MainPageLocators.market)
        click_market.click()
        self.browser.switch_to.window(self.browser.window_handles[-1])
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_pricing(self):
        self.browser.maximize_window()
        click_price = self.browser.find_element(*MainPageLocators.pricing)
        click_price.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_maps(self):
        self.browser.maximize_window()
        click_map = self.browser.find_element(*MainPageLocators.maps)
        click_map.click()
        self.browser.switch_to.window(self.browser.window_handles[-1])
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_initiatives(self):
        self.browser.maximize_window()
        click_initiatives = self.browser.find_element(*MainPageLocators.initiatives)
        click_initiatives.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_partners(self):
        self.browser.maximize_window()
        click_partners = self.browser.find_element(*MainPageLocators.partners)
        click_partners.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_business(self):
        self.browser.maximize_window()
        click_business = self.browser.find_element(*MainPageLocators.business)
        click_business.click()
        self.browser.switch_to.window(self.browser.window_handles[-1])
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_sign_in(self):
        self.browser.maximize_window()
        click_sign_in = self.browser.find_element(*MainPageLocators.sign_in)
        click_sign_in.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_blog(self):
        self.browser.maximize_window()
        click_blog = self.browser.find_element(*MainPageLocators.blog)
        click_blog.click()
        time.sleep(2)
        self.browser.switch_to.window(self.browser.window_handles[-1])
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_autorization(self):
        self.browser.maximize_window()
        input_email = self.browser.find_element(*MainPageLocators.email)
        input_email.send_keys('email')
        time.sleep(2)
        input_password = self.browser.find_element(*MainPageLocators.password)
        input_password.send_keys('password')
        time.sleep(2)
        click_submit = self.browser.find_element(*MainPageLocators.submit)
        click_submit.click()
        time.sleep(2)

    def go_to_input_city(self):
        self.browser.maximize_window()
        click_input_city = self.browser.find_element(*MainPageLocators.input_city)
        click_input_city.click()
        time.sleep(2)
        click_input_city.send_keys('Belgrade')
        time.sleep(2)
        click_input_city.send_keys(Keys.RETURN)
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_home(self):
        self.browser.maximize_window()
        click_home_page = self.browser.find_element(*MainPageLocators.home_page)
        click_home_page.click()
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_support_faq(self):
        self.browser.maximize_window()
        click_support = self.browser.find_element(*MainPageLocators.support)
        click_support.click()
        time.sleep(2)
        click_support_faq = self.browser.find_element(*MainPageLocators.support_faq)
        click_support_faq.click()
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_support_start(self):
        self.browser.maximize_window()
        click_support = self.browser.find_element(*MainPageLocators.support)
        click_support.click()
        time.sleep(2)
        click_support_start = self.browser.find_element(*MainPageLocators.support_start)
        click_support_start.click()
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_support_chat(self):
        self.browser.maximize_window()
        click_support = self.browser.find_element(*MainPageLocators.support)
        click_support.click()
        time.sleep(2)
        click_support_chat = self.browser.find_element(*MainPageLocators.support_chat)
        click_support_chat.click()
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_support_questions(self):
        self.browser.maximize_window()
        click_support = self.browser.find_element(*MainPageLocators.support)
        click_support.click()
        time.sleep(2)
        click_support_questions = self.browser.find_element(*MainPageLocators.support_questions)
        click_support_questions.click()
        time.sleep(5)
        self.browser.switch_to.window(self.browser.window_handles[-1])
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_take_part(self):
        self.browser.maximize_window()
        time.sleep(2)
        click_take_part = self.browser.find_element(*MainPageLocators.take_part)
        click_take_part.click()
        time.sleep(5)
        self.browser.switch_to.window(self.browser.window_handles[-1])
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_search_city(self):
        self.browser.maximize_window()
        click_search_city = self.browser.find_element(*MainPageLocators.input_search_city)
        click_search_city.click()
        time.sleep(5)
        input_search = self.browser.find_element(*MainPageLocators.input_search_city)
        input_search.send_keys('Belgrade')
        time.sleep(5)
        click_button = self.browser.find_element(*MainPageLocators.button_search_city)
        click_button.click()
        time.sleep(5)
        choice_city = self.browser.find_element(*MainPageLocators.choice_city_belgrade)
        choice_city.click()
        time.sleep(5)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_facebook(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,6000)")
        click_close = self.browser.find_element(*MainPageLocators.button_close)
        click_close.click()
        time.sleep(2)
        click_banner = self.browser.find_element(*MainPageLocators.button_banner)
        click_banner.click()
        time.sleep(5)
        click_facebook = self.browser.find_element(*MainPageLocators.facebook)
        click_facebook.click()
        time.sleep(2)
        self.browser.switch_to.window(self.browser.window_handles[-1])
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_twitter(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,6000)")
        click_close = self.browser.find_element(*MainPageLocators.button_close)
        click_close.click()
        time.sleep(2)
        click_banner = self.browser.find_element(*MainPageLocators.button_banner)
        click_banner.click()
        time.sleep(5)
        click_twitter = self.browser.find_element(*MainPageLocators.twitter)
        click_twitter.click()
        time.sleep(2)
        self.browser.switch_to.window(self.browser.window_handles[-1])
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_linkedin(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,6000)")
        click_close = self.browser.find_element(*MainPageLocators.button_close)
        click_close.click()
        time.sleep(2)
        click_banner = self.browser.find_element(*MainPageLocators.button_banner)
        click_banner.click()
        time.sleep(5)
        click_linkedin = self.browser.find_element(*MainPageLocators.linkedin)
        click_linkedin.click()
        time.sleep(2)
        self.browser.switch_to.window(self.browser.window_handles[-1])
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_medium(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,6000)")
        click_close = self.browser.find_element(*MainPageLocators.button_close)
        click_close.click()
        time.sleep(2)
        click_banner = self.browser.find_element(*MainPageLocators.button_banner)
        click_banner.click()
        time.sleep(5)
        click_medium = self.browser.find_element(*MainPageLocators.medium)
        click_medium.click()
        time.sleep(2)
        self.browser.switch_to.window(self.browser.window_handles[-1])
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_telegram(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,6000)")
        click_close = self.browser.find_element(*MainPageLocators.button_close)
        click_close.click()
        time.sleep(2)
        click_banner = self.browser.find_element(*MainPageLocators.button_banner)
        click_banner.click()
        time.sleep(5)
        click_telegram = self.browser.find_element(*MainPageLocators.telegram)
        click_telegram.click()
        time.sleep(2)
        self.browser.switch_to.window(self.browser.window_handles[-1])
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_github(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,6000)")
        click_close = self.browser.find_element(*MainPageLocators.button_close)
        click_close.click()
        time.sleep(2)
        click_banner = self.browser.find_element(*MainPageLocators.button_banner)
        click_banner.click()
        time.sleep(5)
        click_github = self.browser.find_element(*MainPageLocators.git_hub)
        click_github.click()
        time.sleep(2)
        self.browser.switch_to.window(self.browser.window_handles[-1])
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_appstore(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,6000)")
        time.sleep(2)
        click_appstore = self.browser.find_element(*MainPageLocators.app_store)
        click_appstore.click()
        time.sleep(5)
        self.browser.switch_to.window(self.browser.window_handles[-1])
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_google_play(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,6000)")
        time.sleep(2)
        click_google_play = self.browser.find_element(*MainPageLocators.google_play)
        click_google_play.click()
        time.sleep(5)
        self.browser.switch_to.window(self.browser.window_handles[-1])
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_metric(self):
        self.browser.maximize_window()
        time.sleep(2)
        click_location = self.browser.find_element(*MainPageLocators.current_location)
        click_location.click()
        time.sleep(2)
        click_fahreinheit = self.browser.find_element(*MainPageLocators.fahrenheit)
        click_fahreinheit.click()
        time.sleep(2)
        click_celsium = self.browser.find_element(*MainPageLocators.celsium)
        click_celsium.click()
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_learn_more(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,2000)")
        time.sleep(2)
        click_learn_more = self.browser.find_element(*MainPageLocators.learn_more)
        click_learn_more.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_current_weather(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,1800)")
        time.sleep(2)
        click_current_weather = self.browser.find_element(*MainPageLocators.current_weather)
        click_current_weather.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_hourly_forecast(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,1800)")
        time.sleep(2)
        click_hourly_forecast = self.browser.find_element(*MainPageLocators.hourly_forecast)
        click_hourly_forecast.click()
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_daily_forecast(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,1800)")
        time.sleep(2)
        click_daily_forecast = self.browser.find_element(*MainPageLocators.daily_forecast)
        click_daily_forecast.click()
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_climatic_forecast(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,1800)")
        time.sleep(2)
        click_climatic_forecast = self.browser.find_element(*MainPageLocators.climatic_forecast)
        click_climatic_forecast.click()
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_historical_weather(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,1800)")
        time.sleep(2)
        click_historical_weather = self.browser.find_element(*MainPageLocators.historical_weather)
        click_historical_weather.click()
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_footer_api(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,6000)")
        time.sleep(2)
        click_footer_api = self.browser.find_element(*MainPageLocators.footer_api)
        click_footer_api.click()
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_footer_history(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,6000)")
        time.sleep(2)
        click_footer_history = self.browser.find_element(*MainPageLocators.footer_history)
        click_footer_history.click()
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_footer_map(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,6000)")
        time.sleep(2)
        click_footer_map = self.browser.find_element(*MainPageLocators.footer_map)
        click_footer_map.click()
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_footer_dashboard(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,6000)")
        time.sleep(2)
        click_footer_dash = self.browser.find_element(*MainPageLocators.footer_dash)
        click_footer_dash.click()
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_footer_widgets(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,6000)")
        time.sleep(2)
        click_footer_widgets = self.browser.find_element(*MainPageLocators.footer_widgets)
        click_footer_widgets.click()
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_footer_our_technology(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,6000)")
        time.sleep(2)
        click_footer_our_technology = self.browser.find_element(*MainPageLocators.footer_our_technology)
        click_footer_our_technology.click()
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_footer_weather_data(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,6000)")
        time.sleep(2)
        click_footer_weather_data = self.browser.find_element(*MainPageLocators.footer_weather_data)
        click_footer_weather_data.click()
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_footer_weather_stations(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,6000)")
        time.sleep(2)
        click_footer_weather_stations = self.browser.find_element(*MainPageLocators.footer_weather_station)
        click_footer_weather_stations.click()
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_footer_price(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,5500)")
        time.sleep(2)
        click_footer_price = self.browser.find_element(*MainPageLocators.footer_price)
        click_footer_price.click()
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_footer_how_to_start(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,5500)")
        time.sleep(2)
        click_footer_start = self.browser.find_element(*MainPageLocators.footer_how_to_start)
        click_footer_start.click()
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_footer_subscribe(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,5500)")
        time.sleep(2)
        click_footer_subscribe = self.browser.find_element(*MainPageLocators.footer_subscribe)
        click_footer_subscribe.click()
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_footer_terms(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,6000)")
        time.sleep(2)
        click_footer_terms = self.browser.find_element(*MainPageLocators.footer_terms)
        click_footer_terms.click()
        time.sleep(2)
        self.browser.switch_to.window(self.browser.window_handles[-1])
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_footer_privacy(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,6000)")
        time.sleep(2)
        click_footer_privacy = self.browser.find_element(*MainPageLocators.footer_privacy)
        click_footer_privacy.click()
        time.sleep(2)
        self.browser.switch_to.window(self.browser.window_handles[-1])
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_footer_website(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,6000)")
        time.sleep(2)
        click_footer_website = self.browser.find_element(*MainPageLocators.footer_website)
        click_footer_website.click()
        time.sleep(2)
        self.browser.switch_to.window(self.browser.window_handles[-1])
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_footer_about_us(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,6000)")
        time.sleep(2)
        click_footer_about_us = self.browser.find_element(*MainPageLocators.footer_about_us)
        click_footer_about_us.click()
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_footer_blog(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,6000)")
        time.sleep(2)
        click_footer_blog = self.browser.find_element(*MainPageLocators.footer_blog)
        click_footer_blog.click()
        time.sleep(2)
        self.browser.switch_to.window(self.browser.window_handles[-1])
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_footer_for_business(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,6000)")
        time.sleep(2)
        click_footer_for_business = self.browser.find_element(*MainPageLocators.footer_for_business)
        click_footer_for_business.click()
        time.sleep(2)
        self.browser.switch_to.window(self.browser.window_handles[-1])
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_footer_chat_bot(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,6000)")
        time.sleep(2)
        click_footer_chat_bot = self.browser.find_element(*MainPageLocators.footer_chat_bot)
        click_footer_chat_bot.click()
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_footer_ask_questions(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,6000)")
        time.sleep(2)
        click_footer_ask_questions = self.browser.find_element(*MainPageLocators.footer_ask_questions)
        click_footer_ask_questions.click()
        time.sleep(2)
        self.browser.switch_to.window(self.browser.window_handles[-1])
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_hourly_weather_data(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,2200)")
        time.sleep(2)
        click_hourly_weather_data = self.browser.find_element(*MainPageLocators.hourly_weather_data)
        click_hourly_weather_data.click()
        time.sleep(2)
        self.browser.switch_to.window(self.browser.window_handles[-1])
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_daily_weather_data(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,2200)")
        time.sleep(2)
        click_daily_weather_data = self.browser.find_element(*MainPageLocators.daily_weather_data)
        click_daily_weather_data.click()
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_month_weather_data(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,2200)")
        time.sleep(2)
        click_month_weather_data = self.browser.find_element(*MainPageLocators.month_weather_data)
        click_month_weather_data.click()
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_historical_weather_data(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,2200)")
        time.sleep(2)
        click_historical_weather_data = self.browser.find_element(*MainPageLocators.historical_weather_data)
        click_historical_weather_data.click()
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_minute_forecast(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,2200)")
        time.sleep(2)
        click_minute_forecast = self.browser.find_element(*MainPageLocators.minute_forecast)
        click_minute_forecast.click()
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_ai_bot(self):
        self.browser.maximize_window()
        time.sleep(2)
        click_ai_bot = self.browser.find_element(*MainPageLocators.ai_bot)
        click_ai_bot.click()
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_view_solutions(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,1500)")
        time.sleep(2)
        click_view_solutions = self.browser.find_element(*MainPageLocators.view_solutions)
        click_view_solutions.click()
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_read_more(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,1500)")
        time.sleep(2)
        click_read_more = self.browser.find_element(*MainPageLocators.read_more)
        click_read_more.click()
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_connect(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,1500)")
        time.sleep(2)
        click_connect = self.browser.find_element(*MainPageLocators.connect)
        click_connect.click()
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_contact_us(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,1500)")
        time.sleep(2)
        click_contact_us = self.browser.find_element(*MainPageLocators.contact_us)
        click_contact_us.click()
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_solar_panel(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,1300)")
        time.sleep(2)
        click_solar_panel = self.browser.find_element(*MainPageLocators.solar_panel)
        click_solar_panel.click()
        time.sleep(2)
        self.browser.switch_to.window(self.browser.window_handles[-1])
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_solar_irradiance(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,1300)")
        time.sleep(2)
        click_solar_irradiance = self.browser.find_element(*MainPageLocators.solar_irradiance)
        click_solar_irradiance.click()
        time.sleep(2)
        self.browser.switch_to.window(self.browser.window_handles[-1])
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_global_weather(self):
        self.browser.maximize_window()
        self.browser.execute_script("window,scrollTo (0,1300)")
        time.sleep(2)
        click_global_weather = self.browser.find_element(*MainPageLocators.global_weather)
        click_global_weather.click()
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_apis(self):
        self.browser.maximize_window()
        time.sleep(2)
        self.browser.execute_script("window,scrollTo (0,1150)")
        time.sleep(2)
        click_apis = self.browser.find_element(*MainPageLocators.apis)
        click_apis.click()
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_bulks(self):
        self.browser.maximize_window()
        time.sleep(2)
        self.browser.execute_script("window,scrollTo (0,1200)")
        time.sleep(2)
        click_bulks = self.browser.find_element(*MainPageLocators.bulks)
        click_bulks.click()
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_apis_histories(self):
        self.browser.maximize_window()
        time.sleep(2)
        self.browser.execute_script("window,scrollTo (0,1150)")
        time.sleep(2)
        click_apis_histories = self.browser.find_element(*MainPageLocators.apis_histories)
        click_apis_histories.click()
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_market_zip_codes(self):
        self.browser.maximize_window()
        time.sleep(2)
        self.browser.execute_script("window,scrollTo (0,1150)")
        time.sleep(2)
        click_market_zip_codes = self.browser.find_element(*MainPageLocators.market_zip_codes)
        click_market_zip_codes.click()
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_fly_bulks(self):
        self.browser.maximize_window()
        time.sleep(2)
        self.browser.execute_script("window,scrollTo (0,1150)")
        time.sleep(2)
        click_fly_bulks = self.browser.find_element(*MainPageLocators.fly_bulks)
        click_fly_bulks.click()
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_one_call_api(self):
        self.browser.maximize_window()
        time.sleep(2)
        self.browser.execute_script("window,scrollTo (0,500)")
        time.sleep(2)
        click_one_call_api = self.browser.find_element(*MainPageLocators.one_call_api)
        click_one_call_api.click()
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_professional_collections(self):
        self.browser.maximize_window()
        time.sleep(2)
        self.browser.execute_script("window,scrollTo (0,1000)")
        time.sleep(2)
        click_professional_collections = self.browser.find_element(*MainPageLocators.professional_collections)
        click_professional_collections.click()
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_how_to_obtain_api(self):
        self.browser.maximize_window()
        time.sleep(2)
        self.browser.execute_script("window,scrollTo (0,1300)")
        time.sleep(2)
        click_how_to_obtain_api = self.browser.find_element(*MainPageLocators.how_to_obtain_api)
        click_how_to_obtain_api.click()
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_how_to_obtain_bulk(self):
        self.browser.maximize_window()
        time.sleep(2)
        self.browser.execute_script("window,scrollTo (0,1300)")
        time.sleep(2)
        click_how_to_obtain_bulk = self.browser.find_element(*MainPageLocators.how_to_obtain_bulk)
        click_how_to_obtain_bulk.click()
        time.sleep(2)
        return LoginPage(browser=self.browser, url=self.browser.current_url)

