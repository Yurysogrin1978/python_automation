pythonimport pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=en,
                     help="Choose your language")


@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    fp = webdriver.FirefoxProfile()
    user_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\n Starting Chrome..")
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\n Starting Firefox..")
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--You should choose browser: Chrome or Firebox")
    yield browser
    print("\n quit browser..")
    browser.quit()
