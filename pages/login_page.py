from base.base_class import BasePage
from locators.locator import MainPageLocators



class LoginPage(BasePage):
#Guide
    def get_click_guide_page(self):
        self.get_click_guide()

    def get_click_guide(self):
        assert MainPageLocators.guide.is_displayed(),"Button Guide is present"

    def test_current_url_guide(self):
        try:
            assert "https://openweathermap.org/guide" in self.url == 'https://openweathermap.org/guide'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#API
    def get_click_api_page(self):
        self.get_click_api()

    def get_click_api(self):
        assert MainPageLocators.api.is_displayed(),"Button API is present"

    def test_current_url_api(self):
        try:
            assert "https://openweathermap.org/api" in self.url == 'https://openweathermap.org/api'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#Dashboard
    def get_click_dashboard_page(self):
        self.get_click_dashboard()

    def get_click_dashboard(self):
        assert MainPageLocators.dashboard.is_displayed(),"Button Dashboard is present"

    def test_current_url_dashboard(self):
        try:
            assert "https://openweathermap.org/weather-dashboard" in self.url == 'https://openweathermap.org/weather-dashboard'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#Marketplace
    def get_click_market_page(self):
        self.get_click_market()

    def get_click_market(self):
        assert MainPageLocators.market.is_displayed(), "Button Marketplace is present"

    def test_current_url_market(self):
        try:
            assert "https://home.openweathermap.org/marketplace" in self.url == 'https://home.openweathermap.org/marketplace'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#Pricing
    def get_click_pricing_page(self):
        self.get_click_pricing()

    def get_click_pricing(self):
        assert MainPageLocators.pricing.is_displayed(), "Button Pricing is present"

    def test_current_url_pricing(self):
        try:
            assert "https://openweathermap.org/price" in self.url == 'https://openweathermap.org/price'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#Maps
    def get_click_maps_page(self):
        self.get_click_maps()

    def get_click_maps(self):
        assert MainPageLocators.maps.is_displayed(), "Button Maps is present"

    def test_current_url_maps(self):
        try:
            assert "https://openweathermap.org/weathermap" in self.url == 'https://openweathermap.org/weathermap'
            print("URL не соответствует ожидаемому")
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#Our Initiative
    def get_click_initiatives_page(self):
        self.get_click_initiatives()

    def get_click_initiatives(self):
        assert MainPageLocators.initiatives.is_displayed(), "Button Maps is present"

    def test_current_url_initiatives(self):
        try:
            assert "https://openweathermap.org/our-initiatives" in self.url == 'https://openweathermap.org/our-initiatives'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#Partners
    def get_click_partners_page(self):
        self.get_click_partners()

    def get_click_partners(self):
        assert MainPageLocators.partners.is_displayed(), "Button Partners is present"

    def test_current_url_partners(self):
        try:
            assert "https://openweathermap.org/examples" in self.url == 'https://openweathermap.org/examples'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#For business
    def get_click_business_page(self):
        self.get_click_business()

    def get_click_business(self):
        assert MainPageLocators.business.is_displayed(), "Button For Business is present"

    def test_current_url_business(self):
        try:
            assert "https://openweather.co.uk/" in self.url == 'https://openweather.co.uk/'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#Sign In
    def get_click_sign_in_page(self):
        self.get_click_sign_in()

    def get_click_sign_in(self):
        assert MainPageLocators.sign_in.is_displayed(), "Button For Business is present"

    def test_current_url_sign_in(self):
        try:
            assert "https://home.openweathermap.org/users/sign_in" in self.url == 'https://home.openweathermap.org/users/sign_in'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#Blog
    def get_click_blog_page(self):
        self.get_click_blog()

    def get_click_blog(self):
        assert MainPageLocators.blog.is_displayed(), "Button For Business is present"

    def test_current_url_blog(self):
        try:
            assert "https://openweather.co.uk/blog/category/weather" in self.url == 'https://openweather.co.uk/blog/category/weather'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#Sign in(Autorization)
    def get_email_form(self):
        assert MainPageLocators.email.is_displayed(), "The email form is present"

    def get_password_form(self):
        assert MainPageLocators.password.is_displayed(), "The password form is present"

    def test_current_url_autorization(self):
        try:
            assert "https://home.openweathermap.org/" in self.url == 'https://home.openweathermap.org/'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#Input "Weather in your city"
    def get_click_city_page(self):
        self.get_input_city_form()
    def get_input_city_form(self):
        assert MainPageLocators.input_city.is_displayed(), "The input city form is present"

    def test_current_url_weather_city(self):
        try:
            assert "https://openweathermap.org/find?q=Belgrade" in self.url == 'https://openweathermap.org/find?q=Belgrade'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#Home page
    def get_click_home_page(self):
        self.get_click_home()
    def get_click_home(self):
        assert MainPageLocators.home_page.is_displayed(), "The home page form is present"

    def test_current_url_home_page(self):
        try:
            assert "https://openweathermap.org/" in self.url == 'https://openweathermap.org/'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#Support(FAQ)
    def get_click_support_faq(self):
        self.get_click_support()
        self.get_click_faq()

    def get_click_support(self):
        assert MainPageLocators.support.is_displayed(), "The Support is present"

    def get_click_faq(self):
        assert MainPageLocators.support_faq.is_displayed(), "The FAQ is present"

    def test_current_url_support_faq(self):
        try:
            assert "https://openweathermap.org/faq" in self.url == 'https://openweathermap.org/faq'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#Support(How to start)
    def get_click_support_start(self):
        self.get_click_support()
        self.get_click_start()

    def get_click_support(self):
        assert MainPageLocators.support.is_displayed(), "The Support is present"

    def get_click_start(self):
        assert MainPageLocators.support_start.is_displayed(), "The How to Start is present"

    def test_current_url_support_start(self):
        try:
            assert "https://openweathermap.org/appid" in self.url == 'https://openweathermap.org/appid'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#Support (ChatBot Assistant)
    def get_click_support_chat(self):
        self.get_click_support()
        self.get_click_chat()

    def get_click_support(self):
        assert MainPageLocators.support.is_displayed(), "The Support is present"

    def get_click_chat(self):
        assert MainPageLocators.support_chat.is_displayed(), "The How to Start is present"

    def test_current_url_support_chat_bot(self):
        try:
            assert "https://openweathermap.org/chat" in self.url == 'https://openweathermap.org/chat'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#Support(Ask the questions)

    def get_click_support_questions(self):
        self.get_click_support()
        self.get_click_questions()

    def get_click_support(self):
        assert MainPageLocators.support.is_displayed(), "The Support is present"

    def get_click_questions(self):
        assert MainPageLocators.support_questions.is_displayed(), "The questions is present"

    def test_current_url_support_questions(self):
        try:
            assert "https://home.openweathermap.org/questions" in self.url == 'https://home.openweathermap.org/questions'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#Take Part

    def get_click_take_part(self):
        self.get_click_take()
    def get_click_take(self):
        assert MainPageLocators.take_part.is_displayed(), "The home page form is present"

    def test_current_url_take_part(self):
        try:
            assert "https://challenge.openweather.co.uk/" in self.url == 'https://challenge.openweather.co.uk/'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#Search City

    def get_click_search_city(self):
        self.get_click_input_city()
        self.get_click_search_city()
        self.get_click_city()

    def get_click_input_city(self):
        assert MainPageLocators.input_search_city.is_displayed(), "The Input is present"

    def get_click_search_city(self):
        assert MainPageLocators.button_search_city.is_displayed(), "The Button is present"

    def get_click_city(self):
        assert MainPageLocators.choice_city_belgrade.is_displayed(), "The Choice City Belgrade is present"

    def test_current_url_seacrh_city(self):
        try:
            assert "https://openweathermap.org/city/792680" in self.url == 'https://openweathermap.org/city/792680'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#Facebook

    def get_click_facebook_page(self):
        self.get_click_banner()
        self.get_click_facebook()

    def get_click_banner(self):
        assert MainPageLocators.button_banner.is_displayed(), "The Button banner form is present"
    def get_click_facebook(self):
        assert MainPageLocators.facebook.is_displayed(), "The Facebook page form is present"

    def test_current_url_facebook(self):
        try:
            assert "https://www.facebook.com/groups/2707489730213" in self.url == 'https://www.facebook.com/groups/2707489730213'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#Twitter


    def get_click_twitter_page(self):
        self.get_click_banner()
        self.get_click_twitter()

    def get_click_banner(self):
        assert MainPageLocators.button_banner.is_displayed(), "The Button banner form is present"
    def get_click_twitter(self):
        assert MainPageLocators.twitter.is_displayed(), "The Twitter page form is present"

    def test_current_url_twitter(self):
        try:
            assert "https://twitter.com/OpenWeatherMap" in self.url == 'https://twitter.com/OpenWeatherMap'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#LinkedIn

    def get_click_linkedin_page(self):
        self.get_click_banner()
        self.get_click_linkedin()

    def get_click_banner(self):
        assert MainPageLocators.button_banner.is_displayed(), "The Button banner form is present"
    def get_click_linkedin(self):
        assert MainPageLocators.linkedin.is_displayed(), "The Linkedin page form is present"

    def test_current_url_linkedin(self):
        try:
            assert "https://www.linkedin.com/company/9816754" in self.url == 'https://www.linkedin.com/company/9816754'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#Medium

    def get_click_medium_page(self):
        self.get_click_banner()
        self.get_click_medium()

    def get_click_banner(self):
        assert MainPageLocators.button_banner.is_displayed(), "The Button banner form is present"
    def get_click_medium(self):
        assert MainPageLocators.medium.is_displayed(), "The Medium page form is present"

    def test_current_url_medium(self):
        try:
            assert "https://medium.com/@openweathermap" in self.url == 'https://medium.com/@openweathermap'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#Telegram

    def get_click_telegram_page(self):
        self.get_click_banner()
        self.get_click_telegram()

    def get_click_banner(self):
        assert MainPageLocators.button_banner.is_displayed(), "The Button banner form is present"
    def get_click_telegram(self):
        assert MainPageLocators.telegram.is_displayed(), "The Telegram page form is present"

    def test_current_url_telegram(self):
        try:
            assert "https://t.me/openweathermap" in self.url == 'https://t.me/openweathermap'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#GitHub

    def get_click_github_page(self):
        self.get_click_banner()
        self.get_click_github()

    def get_click_banner(self):
        assert MainPageLocators.button_banner.is_displayed(), "The Button banner form is present"
    def get_click_github(self):
        assert MainPageLocators.git_hub.is_displayed(), "The GitHub page form is present"

    def test_current_url_github(self):
        try:
            assert "https://github.com/openweathermap" in self.url == 'https://github.com/openweathermap'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#AppStore

    def get_click_appstore_page(self):
        self.get_click_appstore()

    def get_click_appstore(self):
        assert MainPageLocators.app_store.is_displayed(), "The AppStore page form is present"

    def test_current_url_appstore(self):
        try:
            assert "https://apps.apple.com/gb/app/openweather/id1535923697" in self.url == 'https://apps.apple.com/gb/app/openweather/id1535923697'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#Google Play

    def get_click_google_play_page(self):
        self.get_click_google_play()

    def get_click_google_play(self):
        assert MainPageLocators.google_play.is_displayed(), "The Google Play page form is present"

    def test_current_url_google_play(self):
        try:
            assert "https://play.google.com/store/apps/details?id=uk.co.openweather" in self.url == 'https://play.google.com/store/apps/details?id=uk.co.openweather'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#Current Location

    def get_click_metric_page(self):
        self.get_click_current_location()
        self.get_click_fahreinheit()
        self.get_click_celsium()

    def get_click_current_location(self):
        assert MainPageLocators.current_location.is_displayed(), "The current location is present"

    def get_click_fahreinheit(self):
        assert MainPageLocators.fahrenheit.is_displayed(), "The fahrenheit is present"

    def get_click_celsium(self):
        assert MainPageLocators.celsium.is_displayed(), "The celsium is present"

    def test_current_url_metric(self):
        try:
            assert "https://openweathermap.org/city/565197" in self.url == 'https://openweathermap.org/city/565197'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#Learn More

    def get_click_learn_more_page(self):
        self.get_click_learn_more()
    def get_click_learn_more(self):
        assert MainPageLocators.learn_more.is_displayed(), "The home page form is present"

    def test_current_url_learn_more(self):
        try:
            assert "https://openweathermap.org/api#pro" in self.url == 'https://openweathermap.org/api#pro'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#Current weather

    def get_click_current_weather_page(self):
        self.get_click_current_weather()
    def get_click_current_weather(self):
        assert MainPageLocators.current_weather.is_displayed(), "The current weather page is present"

    def test_current_url_current_weather(self):
        try:
            assert "https://openweathermap.org/current" in self.url == 'https://openweathermap.org/current'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#Hourly forecast

    def get_click_hourly_forecast_page(self):
        self.get_click_hourly_forecast()
    def get_click_hourly_forecast(self):
        assert MainPageLocators.hourly_forecast.is_displayed(), "The hourly forecast page is present"

    def test_current_url_hourly_forecast(self):
        try:
            assert "https://openweathermap.org/api/hourly-forecast" in self.url == 'https://openweathermap.org/api/hourly-forecast'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

# Daily forecast

    def get_click_daily_forecast_page(self):
        self.get_click_daily_forecast()
    def get_click_daily_forecast(self):
        assert MainPageLocators.daily_forecast.is_displayed(), "The daily forecast page is present"

    def test_current_url_daily_forecast(self):
        try:
            assert "https://openweathermap.org/forecast16" in self.url == 'https://openweathermap.org/forecast16'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

# Climatic forecast

    def get_click_daily_climatic_page(self):
        self.get_click_climatic_forecast()
    def get_click_climatic_forecast(self):
        assert MainPageLocators.climatic_forecast.is_displayed(), "The climatic forecast page is present"

    def test_current_url_climatic_forecast(self):
        try:
            assert "https://openweathermap.org/api/forecast30" in self.url == 'https://openweathermap.org/api/forecast30'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#Historical weather

    def get_click_historical_weather_page(self):
        self.get_click_historical_weather()
    def get_click_historical_weather(self):
        assert MainPageLocators.historical_weather.is_displayed(), "The historical_weather page is present"

    def test_current_url_historical_weather(self):
        try:
            assert "https://openweathermap.org/history" in self.url == 'https://openweathermap.org/history'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#API(Footer)

    def get_click_footer_api_page(self):
        self.get_click_footer_api()
    def get_click_footer_api(self):
        assert MainPageLocators.footer_api.is_displayed(), "The footer api page is present"

    def test_current_url_footer_api(self):
        try:
            assert "https://openweathermap.org/api#current" in self.url == 'https://openweathermap.org/api#current'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#History(Footer)

    def get_click_footer_history_page(self):
        self.get_click_footer_history()
    def get_click_footer_history(self):
        assert MainPageLocators.footer_history.is_displayed(), "The footer history page is present"

    def test_current_url_footer_history(self):
        try:
            assert "https://openweathermap.org/api#history" in self.url == 'https://openweathermap.org/api#history'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#Map(Footer)

    def get_click_footer_map_page(self):
        self.get_click_footer_map()
    def get_click_footer_map(self):
        assert MainPageLocators.footer_map.is_displayed(), "The footer map page is present"

    def test_current_url_footer_map(self):
        try:
            assert "https://openweathermap.org/api#maps" in self.url == 'https://openweathermap.org/api#maps'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#Dashboard(Footer)

    def get_click_footer_dashboard_page(self):
        self.get_click_footer_dashboard()
    def get_click_footer_dashboard(self):
        assert MainPageLocators.footer_dash.is_displayed(), "The footer dashboard page is present"

    def test_current_url_footer_dashboard(self):
        try:
            assert "https://openweathermap.org/weather-dashboard" in self.url == 'https://openweathermap.org/weather-dashboard'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

# Widgets(Footer)

    def get_click_footer_widgets_page(self):
        self.get_click_footer_widgets()

    def get_click_footer_widgets(self):
        assert MainPageLocators.footer_widgets.is_displayed(), "The footer widgets page is present"

    def test_current_url_footer_widgets(self):
        try:
            assert "https://openweathermap.org/widgets-constructor" in self.url == 'https://openweathermap.org/widgets-constructor'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

# Our technology(Footer)

    def get_click_footer_our_technology_page(self):
        self.get_click_footer_our_technology()

    def get_click_footer_our_technology(self):
        assert MainPageLocators.footer_our_technology.is_displayed(), "The footer Our technology page is present"

    def test_current_url_footer_our_technology(self):
        try:
            assert "https://openweathermap.org/technology" in self.url == 'https://openweathermap.org/technology'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

# Accuracy and quality of weather data(Footer)

    def get_click_footer_weather_data_page(self):
        self.get_click_footer_weather_data()

    def get_click_footer_weather_data(self):
        assert MainPageLocators.footer_weather_data.is_displayed(), "The footer Accuracy and quality of weather data page is present"

    def test_current_url_footer_weather_data(self):
        try:
            assert "https://openweathermap.org/accuracy-and-quality" in self.url == 'https://openweathermap.org/accuracy-and-quality'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

# Connect your weather station(Footer)

    def get_click_footer_weather_stations_page(self):
        self.get_click_footer_weather_stations()

    def get_click_footer_weather_stations(self):
        assert MainPageLocators.footer_weather_station.is_displayed(), "The footer Accuracy and quality of weather data page is present"

    def test_current_url_footer_weather_stations(self):
        try:
            assert "https://openweathermap.org/stations" in self.url == 'https://openweathermap.org/stations'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#Pricing(Footer)
    def get_click_footer_pricing_page(self):
        self.get_click_footer_pricing()

    def get_click_footer_pricing(self):
        assert MainPageLocators.footer_price.is_displayed(), "The footer Pricing page is present"

    def test_current_url_footer_pricing(self):
        try:
            assert "https://openweathermap.org/price" in self.url == 'https://openweathermap.org/price'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#How to start (Footer)
    def get_click_footer_start_page(self):
        self.get_click_footer_start()

    def get_click_footer_start(self):
        assert MainPageLocators.footer_how_to_start.is_displayed(), "The footer How to Start page is present"

    def test_current_url_footer_start(self):
        try:
            assert "https://openweathermap.org/appid" in self.url == 'https://openweathermap.org/appid'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

# Subscribe (Footer)
    def get_click_footer_subscribe_page(self):
        self.get_click_footer_subscribe()

    def get_click_footer_subscribe(self):
        assert MainPageLocators.footer_subscribe.is_displayed(), "The footer Subscribe page is present"

    def test_current_url_footer_subscribe(self):
        try:
            assert "https://home.openweathermap.org/users/sign_up" in self.url == 'https://home.openweathermap.org/users/sign_up'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

# Terms (Footer)
    def get_click_footer_terms_page(self):
        self.get_click_footer_terms()

    def get_click_footer_terms(self):
        assert MainPageLocators.footer_terms.is_displayed(), "The footer Terms page is present"

    def test_current_url_footer_terms(self):
        try:
            assert "https://openweather.co.uk/storage/app/media/Terms/Openweather_terms_and_conditions_of_sale.pdf" in self.url == 'https://openweather.co.uk/storage/app/media/Terms/Openweather_terms_and_conditions_of_sale.pdf'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#Privacy Policy (Footer)
    def get_click_footer_privacy_page(self):
        self.get_click_footer_privacy()

    def get_click_footer_privacy(self):
        assert MainPageLocators.footer_privacy.is_displayed(), "The footer Privacy page is present"

    def test_current_url_footer_privacy(self):
        try:
            assert "https://openweather.co.uk/privacy-policy" in self.url == 'https://openweather.co.uk/privacy-policy'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

# Website terms and conditions (Footer)
    def get_click_footer_website_page(self):
        self.get_click_footer_website()

    def get_click_footer_website(self):
        assert MainPageLocators.footer_website.is_displayed(), "The footer Website page is present"

    def test_current_url_footer_website(self):
        try:
            assert "https://openweather.co.uk/storage/app/media/Terms/Openweather_website_terms_and_conditions_of_use.pdf" in self.url == 'https://openweather.co.uk/storage/app/media/Terms/Openweather_website_terms_and_conditions_of_use.pdf'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

# About Us (Footer)
    def get_click_footer_about_us_page(self):
        self.get_click_footer_about_us()

    def get_click_footer_about_us(self):
        assert MainPageLocators.footer_about_us.is_displayed(), "The footer About Us page is present"

    def test_current_url_footer_about_us(self):
        try:
            assert "https://openweather.co.uk/about" in self.url == 'https://openweather.co.uk/about'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

# Blog (Footer)
    def get_click_footer_blog_page(self):
        self.get_click_footer_blog()

    def get_click_footer_blog(self):
        assert MainPageLocators.footer_about_us.is_displayed(), "The footer Blog page is present"

    def test_current_url_footer_blog(self):
        try:
            assert "https://openweather.co.uk/blog/category/weather" in self.url == 'https://openweather.co.uk/blog/category/weather'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

# For Business (Footer)
    def get_click_footer_for_business_page(self):
        self.get_click_footer_for_business()

    def get_click_footer_for_business(self):
        assert MainPageLocators.footer_about_us.is_displayed(), "The footer For Business page is present"

    def test_current_url_footer_for_business(self):
        try:
            assert "https://openweather.co.uk/" in self.url == 'https://openweather.co.uk/'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

# Chat Bot (Footer)
    def get_click_footer_chat_bot_page(self):
        self.get_click_footer_chat_bot()

    def get_click_footer_chat_bot(self):
        assert MainPageLocators.footer_about_us.is_displayed(), "The footer Chat Bot page is present"

    def test_current_url_footer_chat_bot(self):
        try:
            assert "https://openweathermap.org/chat" in self.url == 'https://openweathermap.org/chat'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

# Ask questions (Footer)
    def get_click_footer_ask_questions_page(self):
        self.get_click_footer_ask_questions()

    def get_click_footer_ask_questions(self):
        assert MainPageLocators.footer_about_us.is_displayed(), "The footer Ask Questions page is present"

    def test_current_url_footer_ask_questions(self):
        try:
            assert "https://home.openweathermap.org/questions" in self.url == 'https://home.openweathermap.org/questions'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

# Hourly (4 days)
    def get_click_hourly_weather_data_page(self):
        self.get_click_hourly_weather_data()

    def get_click_hourly_weather_data(self):
        assert MainPageLocators.hourly_weather_data.is_displayed(), "The Hourly page is present"

    def test_current_url_hourly_weather_data(self):
        try:
            assert "https://openweathermap.org/api/hourly-forecast" in self.url == 'https://openweathermap.org/api/hourly-forecast'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

# Daily (16 days)
    def get_click_daily_weather_data_page(self):
        self.get_click_daily_weather_data()

    def get_click_daily_weather_data(self):
        assert MainPageLocators.daily_weather_data.is_displayed(), "The Daily page is present"

    def test_current_url_daily_weather_data(self):
        try:
            assert "https://openweathermap.org/forecast16" in self.url == 'https://openweathermap.org/forecast16'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

# Month (30 days)
    def get_click_month_weather_data_page(self):
        self.get_click_month_weather_data()

    def get_click_month_weather_data(self):
        assert MainPageLocators.month_weather_data.is_displayed(), "The Month page is present"

    def test_current_url_month_weather_data(self):
        try:
            assert "https://openweathermap.org/api/forecast30" in self.url == 'https://openweathermap.org/api/forecast30'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

# Historical Bulk
    def get_click_historical_weather_data_page(self):
        self.get_click_historical_weather_data()

    def get_click_historical_weather_data(self):
        assert MainPageLocators.historical_weather_data.is_displayed(), "The Historical Bulk page is present"

    def test_current_url_historical_weather_data(self):
        try:
            assert "https://openweathermap.org/history-bulk" in self.url == 'https://openweathermap.org/history-bulk'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

# Minute-by-minute forecast
    def get_click_minute_forecast_page(self):
        self.get_click_minute_forecast()

    def get_click_minute_forecast(self):
        assert MainPageLocators.minute_forecast.is_displayed(), "The Minute Forecast page is present"

    def test_current_url_minute_forecast(self):
        try:
            assert "https://openweathermap.org/api/one-call-3" in self.url == 'https://openweathermap.org/api/one-call-3'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#AI_Bot
    def get_click_ai_bot_page(self):
        self.get_click_ai_bot()

    def get_click_ai_bot(self):
        assert MainPageLocators.ai_bot.is_displayed(), "The AI Bot page is present"

    def test_current_url_ai_bot(self):
        try:
            assert "https://openweathermap.org/support-centre" in self.url == 'https://openweathermap.org/support-centre'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#view_solutions
    def get_click_view_solutions_page(self):
        self.get_click_view_solutions()

    def get_click_view_solutions(self):
        assert MainPageLocators.view_solutions.is_displayed(), "The View solutions page is present"

    def test_current_url_view_solutions(self):
        try:
            assert "https://openweathermap.org/examples" in self.url == 'https://openweathermap.org/examples'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#read_more
    def get_click_read_more_page(self):
        self.get_click_read_more()

    def get_click_read_more(self):
        assert MainPageLocators.read_more.is_displayed(), "The Read more page is present"

    def test_current_url_read_more(self):
        try:
            assert "https://openweathermap.org/examples#google1" in self.url == 'https://openweathermap.org/examples#google1'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#connect
    def get_click_connect_page(self):
        self.get_click_connect()

    def get_click_connect(self):
        assert MainPageLocators.connect.is_displayed(), "The Connect page is present"

    def test_current_url_connect(self):
        try:
            assert "https://openweathermap.org/stations" in self.url == 'https://openweathermap.org/stations'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#contact_us
    def get_click_contact_us_page(self):
        self.get_click_contact_us()

    def get_click_contact_us(self):
        assert MainPageLocators.contact_us.is_displayed(), "The Contact us page is present"

    def test_current_url_contact_us(self):
        try:
            assert "https://openweathermap.org/stations" in self.url == 'https://openweathermap.org/stations'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#solar_panel
    def get_click_solar_panel_page(self):
        self.get_click_solar_panel()

    def get_click_solar_panel(self):
        assert MainPageLocators.solar_panel.is_displayed(), "The Solar panel page is present"

    def test_current_url_solar_panel(self):
        try:
            assert "https://openweathermap.org/api/solar-panels-and-energy-prediction" in self.url == 'https://openweathermap.org/api/solar-panels-and-energy-prediction'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

#solar_irradiance
    def get_click_solar_irradiance_page(self):
        self.get_click_solar_irradiance()

    def get_click_solar_irradiance(self):
        assert MainPageLocators.solar_irradiance.is_displayed(), "The Solar irradiance page is present"

    def test_current_url_solar_irradiance(self):
        try:
            assert "https://openweathermap.org/api/solar-energy-prediction" in self.url == 'https://openweathermap.org/api/solar-energy-prediction'
        except AssertionError:
            print("URL не соответствует ожидаемому")
        else:
            print("URL соответствует ожидаемому")

