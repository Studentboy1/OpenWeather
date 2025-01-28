from selenium.webdriver.common.by import By

class MainPageLocators():
    guide = (By.XPATH,"//nav[@id='nav-website']//a[@href='/guide']")
    api = (By.XPATH,"//nav[@id='nav-website']//a[@href='/api']")
    dashboard = (By.XPATH,"//nav[@id='nav-website']//a[@href='/weather-dashboard']")
    market = (By.XPATH,"//nav[@id='nav-website']//a[@href='https://home.openweathermap.org/marketplace']")
    pricing = (By.XPATH, "//nav[@id='nav-website']//a[@href='/price']")
    maps = (By.XPATH, "//nav[@id='nav-website']//a[@href='/weathermap']")
    initiatives = (By.XPATH, "//nav[@id='nav-website']//a[@href='/our-initiatives']")
    partners = (By.XPATH, "//nav[@id='nav-website']//a[@href='/examples']")
    business = (By.XPATH, "//nav[@id='nav-website']//a[@href='https://openweather.co.uk']")
    sign_in = (By.XPATH,"//nav[@id='nav-website']//a[@href='https://openweathermap.org/home/sign_in']")
    blog = (By.XPATH,"//nav[@id='nav-website']//a[@href='https://openweather.co.uk/blog/category/weather']")
    email = (By.CSS_SELECTOR,"#user_email")
    password = (By.CSS_SELECTOR,"#user_password")
    submit = (By.XPATH,"//input[@class='btn btn-default btn-color']")
    input_city = (By.XPATH,"//input[@name='q']")
    home_page = (By.XPATH,"//nav[@id='nav-website']//img[@src='/themes/openweathermap/assets/img/logo_white_cropped.png']")
    support = (By.CSS_SELECTOR,"#support-dropdown")
    support_faq = (By.XPATH,"//ul[@class='dropdown-menu dropdown-visible']//a[@href='/faq']")
    support_start = (By.XPATH,"//ul[@class='dropdown-menu dropdown-visible']//a[@href='/appid']")
    support_chat = (By.XPATH, "//ul[@class='dropdown-menu dropdown-visible']//a[@href='/chat']")
    support_questions = (By.XPATH, "//ul[@class='dropdown-menu dropdown-visible']//a[@href='https://home.openweathermap.org/questions']")
    take_part = (By.XPATH, "//div[@class='left-section']//a[@href='https://challenge.openweather.co.uk/']")
    input_search_city = (By.XPATH,"//input[@placeholder='Search city']")
    button_search_city = (By.XPATH, "//button[@class='button-round dark']")
    choice_city_belgrade = (By.XPATH,"//ul[@class='search-dropdown-menu']//span[@style='width: 140px;']")
    button_close = (By.XPATH,"//span[@class='close-btn']")
    button_banner = (By.XPATH,"//button[@class='gdpr-banner__button--dismiss']")
    facebook = (By.XPATH,"//div[@class='social']//img[@alt='facebook icon']")
    twitter = (By.XPATH,"//div[@class='social']//img[@alt='x icon']")
    linkedin = (By.XPATH,"//div[@class='social']//img[@alt='linkedin icon']")
    medium = (By.XPATH, "//div[@class='social']//img[@alt='medium icon']")
    telegram = (By.XPATH, "//div[@class='social']//img[@alt='telegram icon']")
    git_hub = (By.XPATH, "//div[@class='social']//img[@alt='github icon']")
    app_store = (By.XPATH,"//div[@class='footer-section']//img[@alt='Get it on AppStore']")
    google_play = (By.XPATH, "//div[@class='footer-section']//img[@alt='Get it on Google Play']")
    current_location = (By.XPATH,"//div[@class='control-el']")
    fahrenheit = (By.XPATH, "//div[@class='switch-container']//div[@class='slideRight']")
    celsium = (By.XPATH, "//div[@class='switch-container']//div[@class='slideLeft']")
    learn_more = (By.XPATH, "//a[@class='ow-btn round btn-black']")
    current_weather = (By.XPATH, "//div//img[@src='/themes/openweathermap/assets/img/landing/icon-1.png']")
    hourly_forecast = (By.XPATH, "//div//img[@src='/themes/openweathermap/assets/img/landing/icon-2.png']")
    daily_forecast = (By.XPATH, "//div//img[@src='/themes/openweathermap/assets/img/landing/icon-3.png']")
    climatic_forecast = (By.XPATH, "//div//img[@src='/themes/openweathermap/assets/img/landing/icon-4.png']")
    historical_weather = (By.XPATH, "//div//img[@src='/themes/openweathermap/assets/img/landing/icon-5.png']")
    footer_api = (By.XPATH, "//div[@class='footer-section']//a[@href='/api#current']")
    footer_history = (By.XPATH, "//div[@class='footer-section']//a[@href='/api#history']")
    footer_map = (By.XPATH, "//div[@class='footer-section']//a[@href='/api#maps']")
    footer_dash = (By.XPATH, "//div[@class='footer-section']//a[@href='/weather-dashboard']")
    footer_widgets = (By.XPATH, "//div[@class='footer-section']//a[@href='/widgets-constructor']")
    footer_our_technology = (By.XPATH, "//div[@class='footer-section']//a[@href='/technology']")
    footer_weather_data = (By.XPATH, "//div[@class='footer-section']//a[@href='/accuracy-and-quality']")
    footer_weather_station = (By.XPATH, "//div[@class='footer-section']//a[@href='/stations']")
    footer_price = (By.XPATH, "//div[@class='footer-section']//a[@href='/price']")
    footer_how_to_start = (By.XPATH, "//div[@class='footer-section']//a[@href='/appid']")
    footer_subscribe = (By.XPATH, "//div[@class='footer-section']//a[@href='https://home.openweathermap.org/users/sign_up']")
    footer_terms = (By.XPATH, "//div[@class='footer-section']//a[@href='https://openweather.co.uk/storage/app/media/Terms/Openweather_terms_and_conditions_of_sale.pdf']")
    footer_privacy = (By.XPATH, "//div[@class='footer-section']//a[@href='https://openweather.co.uk/privacy-policy']")
    footer_website = (By.XPATH, "//div[@class='footer-section']//a[@href='https://openweather.co.uk/storage/app/media/Terms/Openweather_website_terms_and_conditions_of_use.pdf']")
    footer_about_us = (By.XPATH, "//div[@class='section-content']//a[@href='/about-us']")
    footer_blog = (By.XPATH, "//div[@class='section-content']//a[@href='https://openweather.co.uk/blog/category/weather']")
    footer_for_business = (By.XPATH, "//div[@class='section-content']//a[@href='https://openweather.co.uk/']")
    footer_chat_bot = (By.XPATH, "//div[@class='section-content']//a[@href='/chat']")
    footer_ask_questions = (By.XPATH, "//div[@class='section-content']//a[@href='https://home.openweathermap.org/questions']")
    hourly_weather_data = (By.XPATH, "//div[@class='section-content grid-container grid-1-1 grid-reverse mobile-padding']//a[@href='/api/hourly-forecast']")
    daily_weather_data = (By.XPATH,"//div[@class='section-content grid-container grid-1-1 grid-reverse mobile-padding']//a[@href='/forecast16']")
    month_weather_data = (By.XPATH,"//div[@class='section-content grid-container grid-1-1 grid-reverse mobile-padding']//a[@href='/api/forecast30']")
    historical_weather_data = (By.XPATH,"//div[@class='section-content grid-container grid-1-1 grid-reverse mobile-padding']//a[@href='/history-bulk']")
    minute_forecast = (By.XPATH,"//div[@class='section-content grid-container grid-1-1 grid-reverse mobile-padding']//a[@href='/api/one-call-3']")
    ai_bot = (By.XPATH, "//div[@id='chat-banner']//a[@class='ow-btn round btn-orange text-center']")
    view_solutions = (By.XPATH,"//div[@class='section-content grid-container grid-1-1 mobile-padding']//a[@href='/examples']")
    read_more = (By.XPATH,"//div[@class='section-content grid-container grid-1-1 mobile-padding']//a[@href='/examples#google1']")
    connect = (By.XPATH,"//div[@class='section-content grid-container grid-1-1 mobile-padding']//a[@href='/stations']")
    contact_us = (By.XPATH,"//div[@class='section-content grid-container grid-1-1 mobile-padding']//a[@href='mailto:info@openweathermap.org']")
    solar_panel = (By.XPATH,"//div[@class='section']//a[@href='/api/solar-panels-and-energy-prediction']")
    solar_irradiance = (By.XPATH,"//div[@class='section']//a[@href='/api/solar-energy-prediction']")
    global_weather = (By.XPATH,"//div[@class='section']//a[@href='/api/push-weather-alerts']")
    apis = (By.XPATH,"//div[@class='section grey-background']//a[@href='/current']")
    bulks = (By.XPATH,"//div[@class='section grey-background']//a[@href='/bulk']")
    apis_histories = (By.XPATH,"//div[@class='section']//a[@href='/api#history']")
    market_zip_codes = (By.XPATH,"//div[@class='section']//a[@href='https://home.openweathermap.org/marketplace']")
    fly_bulks = (By.XPATH,"//div[@class='section']//a[@href='https://home.openweathermap.org/marketplace']")
