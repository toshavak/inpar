def get_driver(config):
    """Returns a WebDriver instance with the given config."""

    driver = None
    if config.browser == "chrome":
        options = webdriver.ChromeOptions()
        if config.headless:
            options.add_argument("--headless")
        if config.proxy:
            options.add_argument("--proxy-server={}".format(config.proxy))
        driver = webdriver.Chrome(options=options)
    elif config.browser == "firefox":
        options = webdriver.FirefoxOptions()
        if config.headless:
            options.add_argument("--headless")
        if config.proxy:
            options.add_argument("--proxy-server={}".format(config.proxy))
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError("Invalid browser: {}".format(config.browser))

    return driver
