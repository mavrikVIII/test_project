import pytest, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language',\
                    action = 'store', \
                    default = "en", \
                    help = "choose language: ru,en")




@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")

    print('browser_name====',browser_name)
    user_language = request.config.getoption("language")


    # browser = webdriver.Chrome(options=options)

    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options = options)

    elif browser_name == "firefox":
        fp = webdriver.Firefox()
        fp.set_preference('intl.accept_languages', user_language)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    time.sleep(5)
    browser.quit()
